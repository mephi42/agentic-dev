#!/bin/sh
set -e -u -x
for env_sh in /etc/dev-env.d/*.sh; do
    if [ -f "$env_sh" ]; then
        . "$env_sh"
    fi
done
mkdir -p /home/user/.ssh/sshd_config.d
echo "SetEnv PATH=$PATH http_proxy=$http_proxy https_proxy=$https_proxy" \
    >/home/user/.ssh/sshd_config.d/env.conf
setsid socat \
    UNIX-LISTEN:/home/user/.ssh/sshd.sock,fork,unlink-early \
    EXEC:"/usr/sbin/sshd -e -i -f /home/user/.ssh/sshd_config",nofork \
    </dev/null >/home/user/.ssh/sshd.log 2>&1 &
exec "$@"
