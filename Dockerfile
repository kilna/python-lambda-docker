FROM alpine:latest
LABEL maintainer="Kilna kilna@kilna.com"
RUN apk add --no-cache --update python py-pip zip &&\
    pip install python-lambda && \
    mkdir /workspace
WORKDIR /workspace
CMD /bin/sh -i
