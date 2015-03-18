#!/usr/bin/env python 

from docker import Client
import re
import os

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.17')

def removecontainer():
	containers = dockercli.containers(all=True)
	nodelist = []
	
	for node in containers:
		for name in node['Names']:
			name = name.replace("/","")
			m = re.match("^nunode[0-9]\d*$", name)
		
		if m:
			nodestop = "docker stop %s" % name
			noderemove = "docker rm %s" % name
			
			os.system(nodestop)
			os.system(noderemove)
			
removecontainer()
