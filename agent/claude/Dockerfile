FROM scratch AS claude
ADD --chmod=755 \
    --checksum=sha256:1e08503dbdf3c2cb0d706d32f3408277388d1c76ef108673e8fe42c1b322925b \
    https://downloads.claude.ai/claude-code-releases/2.1.280/linux-x64/claude \
    /claude

FROM base
COPY --from=claude /claude /usr/bin/claude
ENV DISABLE_AUTOUPDATER=1
ARG REVIEW_PROMPTS_PROJECT=
RUN if [ -n "$REVIEW_PROMPTS_PROJECT" ]; then \
        git clone https://github.com/masoncl/review-prompts \
            /opt/review-prompts && \
        git -C /opt/review-prompts checkout --detach abdb03e8d690; \
    fi
