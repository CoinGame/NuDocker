#!/usr/bin/env python 

from docker import Client
from toolbox import *
import sys

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.17')

#Grab number of containers to create
file, nodenum = sys.argv

#Makin variables and stuff
nodenum = int(nodenum)
i=0
portlist = []


def getunitport(nodename):
	nodename = nodename.lower()
	
	return dockercli.port(nodename, 7895)[0]['HostPort']

#create muliple containers based on the arg provided
while i < nodenum:

	run = "docker run --name nunode%s -t -d -P nodes" % i
	name = "nunode%s" % i
	
	os.system(run)
	
	port = getunitport(name)
	portlist.append("addnode=127.0.0.1:%s" % port)
	
	i = i + 1
	
conf = """
testnet=1
server=1
rpcuser=user
rpcpassword=pass
gen=1
listen=1
rpcallowip=*
"""
#use addnodes to add all the docker containers to the end of the conf file
for port in portlist:
	conf += (port + "\n")

createnudir()

createnuconf(conf)



