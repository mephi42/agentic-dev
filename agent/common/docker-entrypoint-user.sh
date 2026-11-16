#!/bin/bash
set -e -u -x
if [ -n "${REVIEW_PROMPTS_PROJECT:-}" ]; then
    /opt/review-prompts/setup.sh claude "$REVIEW_PROMPTS_PROJECT"
fi
git -C ~ add --no-warn-embedded-repo src/
exec "$@"
