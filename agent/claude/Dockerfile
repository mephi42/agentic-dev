FROM scratch AS claude
ADD --chmod=755 \
    --checksum=sha256:26d020351e8112f4006790f3cfce43b4c9df0c1bb1d0e542364d64151b81d5ba \
    https://downloads.claude.ai/claude-code-releases/2.1.263/linux-x64/claude \
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
