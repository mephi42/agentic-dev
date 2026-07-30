#!/bin/sh
set -e -u -x
if ent=$(getent passwd "$HOST_UID"); then
    userdel "$(echo "$ent" | cut -d: -f1)"
fi
if ent=$(getent group "$HOST_GID"); then
    groupdel "$(echo "$ent" | cut -d: -f1)"
fi
groupadd -g "$HOST_GID" group
if [ -n "${HOST_KVM_GID:-}" ]; then
    groupadd -g "$HOST_KVM_GID" kvm || groupmod -g "$HOST_KVM_GID" kvm
    useradd -g "$HOST_GID" -G "$HOST_KVM_GID" -m -s /bin/bash -u "$HOST_UID" user
else
    useradd -g "$HOST_GID" -m -s /bin/bash -u "$HOST_UID" user
fi
chown user:group /home/user/.cache
exec setpriv --reuid=user --regid=group --init-groups --inh-caps=-all \
         env HOME=/home/user /docker-entrypoint-user.sh "$@"
