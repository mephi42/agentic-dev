FROM scratch AS uv
ADD --checksum=sha256:eadd9d27c134ab5ac1ffd4473b97a741407f3ea238288f03121fc4deddf90220 \
    https://github.com/astral-sh/uv/releases/download/0.13.1/uv-x86_64-unknown-linux-gnu.tar.gz \
    /uv.tar.gz

FROM base
RUN --mount=type=bind,from=uv,source=/uv.tar.gz,target=/tmp/uv.tar.gz \
    tar -xzf /tmp/uv.tar.gz -C /usr/local/bin --strip-components=1 \
        uv-x86_64-unknown-linux-gnu/uv
RUN UV_TOOL_DIR=/opt/uv/tools UV_TOOL_BIN_DIR=/usr/local/bin \
    UV_PYTHON_INSTALL_DIR=/opt/uv/python UV_NO_CACHE=1 \
    uv tool install reflection-mirror==0.1.0
ENV MIRROR_SKIP_UPDATE=1
