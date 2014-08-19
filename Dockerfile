FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y openssh-server software-properties-common python-software-properties language-pack-en nano
RUN apt-add-repository ppa:bitcoin/bitcoin -y

RUN mkdir /var/run/sshd
RUN echo 'root:nubits' | chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config

ADD ./nud /root/nud
ADD /dep.sh /dep.sh
ADD /GenConf.sh /GenConf.sh
ADD /Start.sh /Start.sh

RUN ./dep.sh
RUN ./GenConf.sh
RUN ./Start.sh

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

EXPOSE 7890
EXPOSE 7895
EXPOSE 14001
EXPOSE 15001
EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
