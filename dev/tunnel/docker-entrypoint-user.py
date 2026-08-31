#!/usr/bin/env python3
"""Forward the peer containers' sshd sockets into /sockets"""

import sys
from pathlib import Path
from subprocess import CalledProcessError, Popen, check_output
from threading import Event

import yaml

SOCKETS = Path("/sockets")
TUNNELS = Path("/tunnels.yml")

SSH_OPTIONS = [
    arg
    for option in [
        "BatchMode=yes",
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


def check_output_verbose(argv, **kwargs):
    print("+", argv, file=sys.stderr)
    return check_output(argv, **kwargs)


def main():
    hosts = yaml.safe_load(TUNNELS.read_text()) or {}
    for host, containers in hosts.items():
        try:
            remote_home = check_output_verbose(
                ["ssh", *SSH_OPTIONS, host, "pwd"], text=True
            ).strip()
        except CalledProcessError as e:
            raise SystemExit(f"cannot ssh into {host} unattended") from e
        tunnel_args = ["autossh", "-M", "0", *SSH_OPTIONS]
        for container in containers:
            local_sock = SOCKETS / f"sshd-{container['name']}.sock"
            remote_sock = f"{remote_home}/{container['path']}/dev/home/.ssh/sshd.sock"
            tunnel_args.extend(["-L", f"{local_sock}:{remote_sock}"])
        tunnel_args.extend(["-N", host])
        popen_verbose(tunnel_args)
    Event().wait()


if __name__ == "__main__":
    main()
