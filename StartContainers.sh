sudo docker pull ubuntu:14.04

sudo docker build -t="nodes" .

sudo docker rm -f node1

sudo docker run --name "node1" -t -d -P nodes

cd ~/.nuTESTING

testnetProtocolPort=$(sudo docker port node1 7895)
IFS=':' read -a ExposedTestnetProtocolPort <<< "$testnetProtocolPort"
tnep="${ExposedTestnetProtocolPort[1]}"

echo "connect=127.0.0.1:$tnep" >> nu.conf



sudo docker ps



