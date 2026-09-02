ARG BASE_IMAGE=scratch
FROM ${BASE_IMAGE}
ARG LLVM_VERSION=
RUN if [ -n "$LLVM_VERSION" ]; then \
        apt-get update && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            gnupg \
            lsb-release \
            software-properties-common \
            wget && \
        curl -sSf https://apt.llvm.org/llvm.sh | bash -s -- "$LLVM_VERSION" && \
        apt-get install -y --no-install-recommends \
            "llvm-$LLVM_VERSION" && \
        echo "PATH=/usr/lib/llvm-$LLVM_VERSION/bin:\$PATH" \
            >/etc/profile.d/llvm.sh; \
    fi
ARG RUST_VERSION=
RUN if [ -n "$RUST_VERSION" ]; then \
        apt-get update && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            gzip && \
        triple="$(uname -m)-unknown-linux-gnu" && \
        curl -sSf "https://static.rust-lang.org/dist/rust-$RUST_VERSION-$triple.tar.gz" | \
            tar -xz -C /tmp && \
        "/tmp/rust-$RUST_VERSION-$triple/install.sh" && \
        rm -rf "/tmp/rust-$RUST_VERSION-$triple"; \
    fi
RUN --mount=type=bind,source=packages.txt,target=/tmp/packages.txt \
    apt-get update && \
    xargs apt-get install -y \
        git \
        openssh-server \
        rsync \
        socat \
        sudo \
        tmux \
        </tmp/packages.txt
ARG CCACHE_MAXSIZE=
RUN if [ -n "$CCACHE_MAXSIZE" ]; then \
        if [ -n "$LLVM_VERSION" ]; then \
            for cc in clang clang++; do \
                ln -sf ../../bin/ccache "/usr/lib/ccache/$cc"; \
            done; \
        fi && \
        echo "max_size = $CCACHE_MAXSIZE" >/etc/ccache.conf && \
        echo "PATH=/usr/lib/ccache:\$PATH" >/etc/profile.d/ccache.sh; \
    fi
RUN --mount=type=bind,source=post-install.sh,target=/tmp/post-install.sh \
    sh -e -x /tmp/post-install.sh
COPY fs/ /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
