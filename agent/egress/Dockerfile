FROM ubuntu:24.04
RUN apt-get update && apt-get install -y iproute2 tinyproxy
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf
COPY allow.txt /etc/tinyproxy/allow.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
EXPOSE 8888
ENTRYPOINT ["/docker-entrypoint.sh"]
