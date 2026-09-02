#!/bin/bash
set -e -u -x
export PATH=$HOME/.local/bin:$PATH
if [ -n "${REVIEW_PROMPTS_PROJECT:-}" ]; then
    /opt/review-prompts/setup.sh claude "$REVIEW_PROMPTS_PROJECT"
fi
exec "$@"
