#!/bin/sh
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
EXERCISE=$(CDPATH= cd -- "$HERE/.." && pwd)
PYGEOAPI="${PYGEOAPI:-$EXERCISE/.venv/bin/pygeoapi}"
if [ ! -x "$PYGEOAPI" ]; then
  echo "Missing exercise environment. Run $EXERCISE/setup_pygeoapi.sh first." >&2
  exit 1
fi
cd "$HERE"
export PYTHONPATH="$EXERCISE${PYTHONPATH:+:$PYTHONPATH}"
export PYGEOAPI_CONFIG="$HERE/pygeoapi-config.yml"
export PYGEOAPI_OPENAPI="$HERE/openapi.yml"
"$PYGEOAPI" openapi generate "$PYGEOAPI_CONFIG" --output-file "$PYGEOAPI_OPENAPI"
exec "$PYGEOAPI" serve
