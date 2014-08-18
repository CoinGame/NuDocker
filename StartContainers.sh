
sudo docker build -t="Nodes" .

sudo docker rm -f $(sudo docker ps -a)

clear

sudo docker run --name "Node1" -t -d -n -P Nodes

