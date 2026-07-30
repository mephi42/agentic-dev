FROM ubuntu:24.04
RUN apt-get update && apt-get install -y tinyproxy
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf
COPY allow.txt /etc/tinyproxy/allow.txt
EXPOSE 8888
CMD ["tinyproxy", "-c", "/etc/tinyproxy/tinyproxy.conf", "-d"]
