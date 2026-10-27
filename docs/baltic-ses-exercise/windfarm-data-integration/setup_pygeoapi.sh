#!/bin/sh
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 -m venv "$HERE/.venv"
"$HERE/.venv/bin/python" -m pip install --upgrade pip
"$HERE/.venv/bin/python" -m pip install -r "$HERE/requirements-pygeoapi.txt"
echo "pygeoapi environment ready. Start it with: $HERE/service/run.sh"
