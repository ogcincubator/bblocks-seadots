#!/usr/bin/env bash
# Build and (optionally) publish the SeaDOTs Concept Editor container image.
#
# Usage:
#   ./build-image.sh                       # build ghcr.io/ogcincubator/seadots-concept-editor:dev
#   IMAGE=myrepo/editor TAG=1.0 ./build-image.sh --push
#
# Env:
#   IMAGE  image repository (default ghcr.io/ogcincubator/seadots-concept-editor)
#   TAG    image tag        (default: short git sha, or 'dev')
set -euo pipefail
cd "$(dirname "$0")"

IMAGE="${IMAGE:-ghcr.io/ogcincubator/seadots-concept-editor}"
TAG="${TAG:-$(git rev-parse --short HEAD 2>/dev/null || echo dev)}"
REF="${IMAGE}:${TAG}"

echo "Building ${REF}…"
docker build -t "${REF}" -t "${IMAGE}:latest" .

if [[ "${1:-}" == "--push" ]]; then
  echo "Pushing ${REF}…"
  docker push "${REF}"
  docker push "${IMAGE}:latest"
fi

echo "Done: ${REF}"
