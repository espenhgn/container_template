FROM ubuntu:20.04

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

# check that hadolint gh action complains
RUN apt-get install -y gcc

WORKDIR /tmp
COPY /scripts/apt_get_essential.sh .
RUN bash apt_get_essential.sh
