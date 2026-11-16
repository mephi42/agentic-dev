ARG BASE_IMAGE=scratch
FROM ${BASE_IMAGE}
RUN --mount=type=bind,source=packages.txt,target=/tmp/packages.txt \
    --mount=type=bind,source=packages-localhost.txt,target=/tmp/localhost.txt \
    apt-get update && \
    cat /tmp/packages.txt /tmp/localhost.txt | xargs apt-get install -y
# pip before --break-system-packages rejects the flag but skips the env var:
# https://github.com/pypa/pip/blob/26.2.1/src/pip/_internal/cli/parser.py#L270-L274
RUN --mount=type=bind,source=pip-packages-localhost.txt,target=/tmp/pip-packages.txt \
    if [ -s /tmp/pip-packages.txt ]; then \
        PIP_BREAK_SYSTEM_PACKAGES=1 python3 -m pip install --no-cache-dir \
            -r /tmp/pip-packages.txt; \
    fi
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint-user.sh /docker-entrypoint-user.sh
ENV LANG=C.UTF-8
ENV PATH=/home/user/.local/bin:$PATH
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
