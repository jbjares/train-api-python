FROM python:3.7.2-alpine3.8
LABEL maintainer="luk.zim91@gmail.com"

COPY . /tmp/pht
RUN cd /tmp/pht && \
    python ./run_tests.py && \
    python setup.py install && \
    cd / && \
    rm -rf /tmp/* /var/tmp/* && sync

