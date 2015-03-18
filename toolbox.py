#!/usr/bin/env python 

import os
import shutil
from os.path import expanduser

#Variables and stuff
nudir = expanduser("~") + "/.nuTESTING"

def removenudir():
	shutil.rmtree(nudir)
	
def createnudir():
	if not os.path.exists(nudir):
		os.makedirs(nudir)

def createnuconf(content):
	if not os.path.exists(nudir):
		os.makedirs(nudir)
		nuconf = nudir + "/nu.conf"
		
		with open(nuconf, 'w') as file_:
			file_.write(content)

