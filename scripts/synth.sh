#!/bin/bash

set -euo pipefail
MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$MYDIR/.."

yarn --cwd deploy install --frozen-lockfile
yarn --cwd deploy cdk synth --strict github-metrics
