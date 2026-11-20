#!/usr/bin/env python3
"""Forward the peer containers' sshd sockets into /sockets"""

import sys
from os import environ
from pathlib import Path
from subprocess import Popen
from threading import Event

import yaml

SOCKETS = Path("/sockets")
TUNNELS = Path("/tunnels.yml")

SSH_OPTIONS = [
    arg
    for option in [
        "BatchMode=yes",
        "ControlPath=none",
        "ExitOnForwardFailure=yes",
        "ServerAliveInterval=30",
        "ServerAliveCountMax=3",
        "StreamLocalBindUnlink=yes",
    ]
    for arg in ("-o", option)
]


def popen_verbose(argv, **kwargs):
    print("+", argv, file=sys.stderr)
    return Popen(argv, **kwargs)


def main():
    hosts = yaml.safe_load(TUNNELS.read_text()) or {}
    for host, containers in hosts.items():
        tunnel_args = ["autossh", "-M", "0", *SSH_OPTIONS]
        for container in containers:
            local_sock = SOCKETS / f"sshd-{container['name']}.sock"
            remote_sock = f"{container['dev']}/home/.ssh/sshd.sock"
            tunnel_args.extend(["-L", f"{local_sock}:{remote_sock}"])
        tunnel_args.extend(["-N", host])
        # Restart ssh even when its first run fails: https://sources.debian.org/src/autossh/1.4g-1/autossh.c/#L998-L1010
        popen_verbose(tunnel_args, env={**environ, "AUTOSSH_GATETIME": "0"})
    Event().wait()


if __name__ == "__main__":
    main()
