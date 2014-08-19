sudo docker pull ubuntu:14.04

sudo docker build -t="Nodes" .

sudo docker rm -f $(sudo docker ps -a)

clear

sudo docker run --name "Node1" -t -d -n -P Nodes

sudo docker run --name "Node2" -t -d -n -P Nodes

sudo docker run --name "Node3" -t -d -n -P Nodes

sudo docker ps
