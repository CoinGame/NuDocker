peer-qa-containers
==================

A set of scripts for automating the use of Docker containers with Peershares, Peerunity, etc.

==================

Install Docker

https://docs.docker.com/installation/ubuntulinux/#ubuntu-trusty-1404-lts-64-bit

==================

Clone this repo
  
  $ git clone https://github.com/pennybreak/peer-qa-containers.git

==================

Build the peer-qa image
  
  $ cd peer-qa-containers
  
  $ sudo docker build -t="pennybreak/peer-qa:v1" .

==================

Start new container (deamon mode)
  
  $ sudo docker run -d pennybreak/peer-qa:v1 /bin/sh peer-qa-containers/addcontainer.sh
  
Start container (interactive mode)

  $ sudo docker run -t -i pennybreak/peer-qa:v1 /bin/bash
  

