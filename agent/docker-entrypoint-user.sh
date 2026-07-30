#!/bin/bash
set -e -u -x
export PATH=$HOME/.local/bin:$PATH
exec "$@"
