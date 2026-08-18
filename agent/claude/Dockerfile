FROM ubuntu:24.04 AS claude
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://claude.ai/install.sh | bash -s 2.1.234
RUN mv /root/.local/share/claude/versions/2.1.234 /claude

FROM ubuntu:24.04
RUN --mount=type=bind,from=common,source=packages.txt,target=/tmp/packages.txt \
    apt-get update && xargs apt-get install -y </tmp/packages.txt
COPY --from=claude /claude /usr/bin/claude
COPY --from=common docker-entrypoint.sh /docker-entrypoint.sh
COPY --from=common docker-entrypoint-user.sh /docker-entrypoint-user.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
