FROM ubuntu:14.04


RUN apt-get update
RUN apt-get install -y openssh-server software-properties-common python-software-properties
RUN apt-add-repository ppa:bitcoin/bitcoin -y


RUN mkdir /var/run/sshd
RUN echo 'root:nubits' | chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config
RUN export LC_ALL=C

ADD /dep.sh /dep.sh
ADD /GenConf.sh /GenConf.sh
ADD ./nud /root/nud

RUN ./dep.sh
RUN ./GenConf.sh

EXPOSE 7890
EXPOSE 7895
EXPOSE 14001
EXPOSE 15001
EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
