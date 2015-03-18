#!/usr/bin/env python 

from docker import Client
from os.path import expanduser
import os
import sys

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')

#Grab number of containers to create
file, nodenum = sys.argv

#Makin variables and stuff
nodenum = int(nodenum)
i=0
portlist = []
nuconf = (expanduser("~") + "/.nuTESTING/nu.conf")

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

for port in portlist:
	conf += (port + "\n")

with open(nuconf, 'w') as file_:
    file_.write(conf)



