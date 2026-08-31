#!/bin/sh
set -e -u -x
if ent=$(getent passwd "$HOST_UID"); then
    userdel "$(echo "$ent" | cut -d: -f1)"
fi
if ent=$(getent group "$HOST_GID"); then
    groupdel "$(echo "$ent" | cut -d: -f1)"
fi
groupadd -g "$HOST_GID" group
useradd -g "$HOST_GID" -s /bin/sh -u "$HOST_UID" user
exec setpriv --reuid=user --regid=group --init-groups --inh-caps=-all \
         env HOME=/home/user /docker-entrypoint-user.py
