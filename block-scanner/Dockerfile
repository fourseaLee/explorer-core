FROM ubuntu:18.04

RUN apt-get update && \
        apt-get upgrade -y && \
        apt-get install -y \
        make \
        cmake \
        gcc \
        g++ \
        libcurl4-openssl-dev \
        libevent-dev \
        libpthread-workqueue-dev \
        libgmp-dev \
        libboost-system1.65-dev \
        libboost-program-options1.65-dev \
        libgmpxx4ldbl \
        librdkafka-dev \
        libmysqlclient-dev && \
        rm -rf /var/lib/apt/lists/*


RUN mkdir monitor 

COPY include monitor/include

COPY src monitor/src

COPY conf monitor/conf

COPY CMakeLists.txt monitor/CMakeLists.txt

RUN cd monitor \
    && mkdir bin \
    && cd bin \
    && cmake ../ \
    && make 

ENTRYPOINT ["/monitor/bin/monitor","-c","/monitor/conf/server_main.conf","-l","/monitor/conf/server_log.conf"]

