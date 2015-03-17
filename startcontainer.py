#!/usr/bin/env python 

from docker import Client
import os
import sys

file, nodenum = sys.argv

int(nodenum)
i=0
print nodenum

while i <= nodenum:

	run = "docker run --name nunode%s -t -d -P nodes" % i

	os.system(run)
	
	i = i + 1

