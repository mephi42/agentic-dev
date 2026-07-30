FROM ubuntu:24.04 AS claude
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://claude.ai/install.sh | bash -s 2.1.211
RUN mv /root/.local/share/claude/versions/2.1.211 /claude

FROM ubuntu:24.04
RUN apt-get update && apt-get install -y \
        clang-format \
        git \
        psmisc \
        python3 \
        rsync \
        socat \
        ssh
COPY --from=claude /claude /usr/bin/claude
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint-user.sh /docker-entrypoint-user.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
