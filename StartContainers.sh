sudo docker pull ubuntu:14.04

sudo docker build -t="nodes" .

sudo docker rm -f node1

sudo docker run --name "node1" -t -d -P nodes

sudo docker attach "node1"

sudo docker ps
