# agentic-dev

Run a coding agent in a network-walled container that builds and tests your
code inside network-walled dev containers on one or more remote hosts, all
reached over SSH.

`agentic-dev` is meant to be vendored into a project repo (as a submodule or
subtree). The project must supply source trees and an `agentic-dev.yml`; this
repo supplies the machinery.

## Getting started

1. Scaffold a project. From any agentic-dev checkout, point `setup` at a new
   (non-existent) directory:
   ```
   /path/to/agentic-dev/setup /path/to/myproject
   ```
   This initializes `/path/to/myproject` as a git repo with agentic-dev as a
   submodule and creates the initial layout:
   ```
   /path/to/myproject/
   ├── agentic-dev/          # this repo
   ├── agentic-dev.yml       # your config
   ├── agent -> agentic-dev/agent
   ├── dev   -> agentic-dev/dev
   ├── init  -> agentic-dev/init
   ├── CLAUDE.md             # agent instructions (mounted into the agent)
   └── src/                  # your source trees, one git submodule each
   ```
2. Edit `agentic-dev.yml`. Every option is documented inline in
   [`template/agentic-dev.yml`](template/agentic-dev.yml).
3. Add your source trees as git submodules under `src/`:
   ```
   cd /path/to/myproject && git submodule add <url> src/<name>
   ```
4. Run `./init` on your workstation. This sets up the directories configured
   in `agentic-dev.yml` on the remote hosts. Re-run it whenever you change the
   config.
5. On each host, start the dev container(s) and leave them running:
   ```
   cd <path>/dev && ./run
   ```
6. On your workstation, launch the agent:
   ```
   ./agent/run
   ```
   The agent can `ssh <container-name>` into any dev container to build and
   test.

Talk to the local dev container directly with `dev/ssh [command...]`.

## Networking model

The agent and dev containers have no direct route out. All egress goes through
a proxy that only allows the hostnames derived from your config.

Every container can reach every other container by name, so agents can
cross-build and cross-test across hosts.
