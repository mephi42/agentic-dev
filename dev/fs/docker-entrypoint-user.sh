#!/bin/sh
set -e -u -x
setsid socat \
    UNIX-LISTEN:/home/user/.ssh/sshd.sock,fork,unlink-early \
    EXEC:"/usr/sbin/sshd -e -i -f /home/user/.ssh/sshd_config",nofork \
    </dev/null >/home/user/.ssh/sshd.log 2>&1 &
exec "$@"
