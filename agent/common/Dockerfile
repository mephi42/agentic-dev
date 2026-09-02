ARG BASE_IMAGE=scratch
FROM ${BASE_IMAGE}
RUN --mount=type=bind,source=packages.txt,target=/tmp/packages.txt \
    --mount=type=bind,source=packages-localhost.txt,target=/tmp/localhost.txt \
    apt-get update && \
    cat /tmp/packages.txt /tmp/localhost.txt | xargs apt-get install -y
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint-user.sh /docker-entrypoint-user.sh
ENV PATH=/home/user/.local/bin:$PATH
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
