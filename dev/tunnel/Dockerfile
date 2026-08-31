FROM ubuntu:24.04
RUN apt-get update && apt-get install -y autossh openssh-client python3-yaml
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint-user.py /docker-entrypoint-user.py
ENTRYPOINT ["/docker-entrypoint.sh"]
