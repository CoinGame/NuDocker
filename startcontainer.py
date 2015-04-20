#!/usr/bin/env python 

from toolbox import *
import os
import sys

#Grab number of containers to create
file, nodenum = sys.argv

#Makin variables and stuff
i=0
iplist = []

#create muliple containers based on the arg provided
while i < int(nodenum):

	name = "nunode%s" % i

	os.system("docker run --name %s -t -d -P nodes /root/nud" % name)
	ip = runcommand("docker inspect --format '{{ .NetworkSettings.IPAddress }}' %s" % name)
	
	iplist.append("addnode=%s " % ip.rstrip())
	
	
	i = i + 1
	
conf = """
testnet=1
server=1
rpcuser=user
rpcpassword=pass
gen=1
listen=1
splitsharesoutputs=50000000
rpcallowip=*
"""

#use addnodes to add all the docker containers to the end of the conf file
for ip in iplist:
	conf += (ip + "\n")

createnudir()

createnuconf(conf)



