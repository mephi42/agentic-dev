FROM ubuntu:24.04
RUN apt-get update && apt-get install -y iproute2 tinyproxy
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf
ARG ALLOW_LOCALHOST=
RUN --mount=type=bind,source=allow.txt,target=/allow-base.txt \
    --mount=type=bind,from=agent,source=allow.txt,target=/allow-agent.txt \
    cat /allow-base.txt /allow-agent.txt >/etc/tinyproxy/allow.txt && \
    printf '%s' "$ALLOW_LOCALHOST" >>/etc/tinyproxy/allow.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
EXPOSE 8888
ENTRYPOINT ["/docker-entrypoint.sh"]
