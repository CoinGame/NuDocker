peer-qa-containers
==================

A set of scripts for automating the use of Docker containers with Peershares, Peerunity, etc.

==================

1. Install Docker

https://docs.docker.com/installation/ubuntulinux/#ubuntu-trusty-1404-lts-64-bit

==================

2. Clone this repo
  
  $ git clone https://github.com/pennybreak/peer-qa-containers.git

==================

3. Build the peer-qa image
  
  $ cd peer-qa-containers
  $ sudo docker build -t="pennybreak/peer-qa:v1" .

==================

4. Start new container
  
  $ sudo docker run -d pennybreak/peer-qa:v1 /bin/sh peer-qa-containers/addcontainer.sh
