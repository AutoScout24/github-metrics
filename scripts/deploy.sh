#!/usr/bin/env bash

set -euo pipefail
MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$MYDIR/.."

yarn --cwd deploy install --prod --frozen-lockfile
yarn --cwd deploy cdk deploy --strict --require-approval never --app ./cdk.out github-metrics
