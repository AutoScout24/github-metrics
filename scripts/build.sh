#!/usr/bin/env bash

set -euo pipefail
MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$MYDIR/.."

pipenv install --dev --skip-lock

rm -rf dist
mkdir -p dist
cp src/*.py dist
pipenv run pip install -r src/requirements.txt -t dist
pushd dist && zip -r github-metrics.zip ./** && popd
