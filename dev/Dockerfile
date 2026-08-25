ARG BASE_IMAGE=
FROM ${BASE_IMAGE:-ubuntu:24.04}
ARG LLVM_VERSION=
RUN if [ -n "$LLVM_VERSION" ]; then \
        apt-get update && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            gnupg \
            lsb-release \
            software-properties-common \
            wget && \
        curl -sSf https://apt.llvm.org/llvm.sh | bash -s -- "$LLVM_VERSION"; \
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
RUN --mount=type=bind,source=post-install.sh,target=/tmp/post-install.sh \
    sh -e -x /tmp/post-install.sh
COPY fs/ /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
