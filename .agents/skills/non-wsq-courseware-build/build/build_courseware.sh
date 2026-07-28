#!/usr/bin/env bash
# Single-command aligned build of the NON-WSQ courseware from the single source
# (course_data.py + data_domainN.py). Produces PPT, LP and LG artifacts in the
# course's courseware/ directory, with page-numbered LP/LG contents pages.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SOFFICE="${SOFFICE:-soffice}"

if ! command -v "$SOFFICE" >/dev/null 2>&1 && [[ ! -x "$SOFFICE" ]]; then
  for candidate in \
    "/c/Program Files/LibreOffice/program/soffice.exe" \
    "/mnt/c/Program Files/LibreOffice/program/soffice.exe" \
    "/c/Program Files (x86)/LibreOffice/program/soffice.exe"
  do
    if [[ -x "$candidate" ]]; then
      SOFFICE="$candidate"
      break
    fi
  done
fi
if ! command -v "$SOFFICE" >/dev/null 2>&1 && [[ ! -x "$SOFFICE" ]]; then
  echo "LibreOffice soffice was not found. Install it or set SOFFICE to its executable." >&2
  exit 2
fi

IFS=$'\t' read -r REPO SHORT <<< "$(python3 - "$HERE" <<'PY'
import os, sys
here = sys.argv[1]
sys.path.insert(0, here)
import course_data as C
def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))
print(find_repo(here) + "\t" + C.SHORT_TITLE)
PY
)"
CW="$REPO/courseware"

convert_pdf() {
  local src="$1"
  local dst="${src%.*}.pdf"
  local profile profile_uri
  profile="$(mktemp -d)"
  profile_uri="$(python3 - "$profile" <<'PY'
from pathlib import Path
import sys
print(Path(sys.argv[1]).resolve().as_uri())
PY
)"
  "$SOFFICE" "-env:UserInstallation=$profile_uri" --headless \
    --convert-to pdf --outdir "$CW" "$src" >/dev/null 2>&1 || true
  for _ in $(seq 1 240); do
    if [[ -s "$dst" && "$dst" -nt "$src" ]]; then
      return 0
    fi
    sleep 1
  done
  echo "Timed out converting $src to PDF." >&2
  return 1
}

echo "==> Generate PPT / LP / labs / LG from the single source"
python3 "$HERE/build_slides.py"
python3 "$HERE/build_lesson_plan.py"
python3 "$HERE/build_labs.py"
python3 "$HERE/build_learner_guide.py"

PPT="$(ls -t "$CW"/*.pptx | head -1)"
LP="$CW/LP-$SHORT.docx"
LG="$CW/LG-$SHORT.docx"

echo "==> Render PDFs (pass 1)"
convert_pdf "$PPT"
convert_pdf "$LP"
convert_pdf "$LG"

echo "==> Inject page-numbered Table of Contents (LP + LG)"
python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 2

echo "==> Render PDFs (pass 2 — with built TOC)"
convert_pdf "$LP"
convert_pdf "$LG"

echo "==> Done. Artifacts in courseware/:"
ls -1 "$CW"/*.pptx "$CW"/*.docx "$CW"/*.pdf
