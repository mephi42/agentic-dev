FROM base AS claude
RUN curl -fsSL https://claude.ai/install.sh | bash -s 2.1.234
RUN mv /root/.local/share/claude/versions/2.1.234 /claude

FROM base
COPY --from=claude /claude /usr/bin/claude
