FROM ubuntu:14.04
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8842CE5E
RUN echo deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu trusty main >/etc/apt/sources.list.d/bitcoin.list
RUN apt-get update # 2014-11-01
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get install -y libboost-filesystem1.54.0 libboost-program-options1.54.0 libboost-thread1.54.0
RUN apt-get install -y libdb4.8++
RUN apt-get install -y libcurl4-openssl-dev

COPY ./nud /root/nud
COPY nu.conf /.nuTESTING/nu.conf

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

EXPOSE 7890
EXPOSE 7895
EXPOSE 14001
EXPOSE 14002
EXPOSE 15001
EXPOSE 15002
EXPOSE 22

CMD /root/nud
