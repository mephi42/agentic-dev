#!/usr/bin/env python3
"""Forward the peer containers' sshd sockets into /sockets"""

import shlex
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
        peer_tunnels = []
        for container in containers:
            local_sock = SOCKETS / f"sshd-{container['name']}.sock"
            remote_sock = f"{container['dev']}/home/.ssh/sshd.sock"
            tunnel_args.extend(["-L", f"{local_sock}:{remote_sock}"])
            if container["peer-tunnels"]:
                # Build: dev/run skips the services that have a profile.
                # Recreate: the container outlives the connection that started it.
                peer_tunnels.append(
                    "docker compose --project-directory"
                    f" {shlex.quote(container['dev'])} --profile tunnel"
                    " up --build --force-recreate tunnel &"
                )
        if len(peer_tunnels) > 0:
            # wait returns 0, on which autossh gives up: https://sources.debian.org/src/autossh/1.4g-1/autossh.c/#L1030-L1038
            command = " ".join([*peer_tunnels, "wait; exit 1"])
            tunnel_args.extend([host, command])
        else:
            tunnel_args.extend(["-N", host])
        # Restart ssh even when its first run fails: https://sources.debian.org/src/autossh/1.4g-1/autossh.c/#L999-L1011
        popen_verbose(tunnel_args, env={**environ, "AUTOSSH_GATETIME": "0"})
    Event().wait()


if __name__ == "__main__":
    main()
