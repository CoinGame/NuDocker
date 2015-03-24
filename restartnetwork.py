#!/usr/bin/env python 

from docker import Client
from toolbox import *
import os

runcommand("killall nu")

nodecount = raw_input("Enter number of nodes to create: ")

if nodecount == "":
	nodecount = len(getnodes())


runcommand("rm -rf ~/.nuTESTING")


os.system(os.path.join(os.path.dirname(os.path.abspath(__file__)), "removecontainer.py"))

os.system(os.path.join(os.path.dirname(os.path.abspath(__file__)), "startcontainer.py %s" % nodecount))

