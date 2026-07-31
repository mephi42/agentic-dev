#!/bin/sh
set -e -u -x
# Bind only to the walled network, named walled0 via the compose driver_opts.
walled_ip=$(ip -o -4 addr show walled0 | awk '{print $4; exit}' | cut -d/ -f1)
{ echo "Listen $walled_ip"; cat /etc/tinyproxy/tinyproxy.conf; } >/tmp/tinyproxy.conf
exec tinyproxy -c /tmp/tinyproxy.conf -d
