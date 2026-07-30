FROM ubuntu:24.04
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
RUN --mount=type=bind,source=packages.txt,target=/tmp/packages.txt \
    apt-get update && \
    xargs apt-get install -y \
        git \
        openssh-server \
        rsync \
        socat \
        sudo \
        </tmp/packages.txt
COPY fs/ /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
