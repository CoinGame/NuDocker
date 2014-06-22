# This is a comment
FROM ubuntu:14.04
MAINTAINER pennybreaker <pennybreaker@outlook.com>
RUN apt-get update
RUN apt-get -y install sudo wget nano git build-essential g++ libssl-dev libboost-all-dev
RUN git clone https://github.com/pennybreak/peer-qa-containers.git
RUN cd peer-qa-containers
RUN deps.sh
