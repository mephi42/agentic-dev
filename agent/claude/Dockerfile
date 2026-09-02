FROM scratch AS claude
ADD --chmod=755 \
    --checksum=sha256:704f1334ac65d3e89e1c6c1d7663293ad786a6166afdb71b5075337df630f976 \
    https://downloads.claude.ai/claude-code-releases/2.1.258/linux-x64/claude \
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
