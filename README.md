peer-qa-containers
==================

A set of scripts for automating the use of Docker containers with Peershares, Peerunity, etc.

==================

Install Docker

https://docs.docker.com/installation/ubuntulinux/#ubuntu-trusty-1404-lts-64-bit

==================

Pull down the base Ubuntu 14.04 image from Docker

  $ sudo docker pull ubuntu:14.04
  
Make sure you have the base image with:
  
  $ sudo docker images

==================

Clone this repo
  
  $ git clone https://github.com/pennybreak/peer-qa-containers.git

==================

Build the peer-qa image
  
  $ cd peer-qa-containers
  
  $ sudo docker build -t="pennybreak/peer-qa:v1" .

==================

Start new container (deamon mode)
  
  $ sudo docker run -d pennybreak/peer-qa:v1 /bin/sh /peer-qa-containers/addcontainer.sh
  
Start container (interactive mode)

  $ sudo docker run -t -i pennybreak/peer-qa:v1 /bin/bash
  
List running containers

  $ sudo docker ps
  
View container log (deamon mode)

  $ sudo docker logs [container name]
  
  
