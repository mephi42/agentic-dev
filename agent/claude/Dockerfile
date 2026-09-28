FROM scratch AS claude
ADD --chmod=755 \
    --checksum=sha256:1859583ce32920595c61ef868bee52e1b1594f7486db209935e01f1e5e804ae2 \
    https://downloads.claude.ai/claude-code-releases/2.1.283/linux-x64/claude \
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
