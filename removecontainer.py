#!/usr/bin/env python 

import re
import os
from toolbox import *


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
