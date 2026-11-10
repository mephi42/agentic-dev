FROM scratch AS claude
ADD --chmod=755 \
    --checksum=sha256:bfb3703ad5380242328459bc62ada4bde8ae7ba57c6e1eeadb9c00e08874c478 \
    https://downloads.claude.ai/claude-code-releases/2.1.322/linux-x64/claude \
    /claude

FROM base
COPY --from=claude /claude /usr/bin/claude
ENV CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
ARG REVIEW_PROMPTS_PROJECT=
RUN if [ -n "$REVIEW_PROMPTS_PROJECT" ]; then \
        git clone https://github.com/masoncl/review-prompts \
            /opt/review-prompts && \
        git -C /opt/review-prompts checkout --detach abdb03e8d690; \
    fi
