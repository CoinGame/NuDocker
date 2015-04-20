#!/usr/bin/env python 

import os
import re
import random
import shutil
import subprocess
import simplejson as json
from os.path import expanduser
from bitcoinrpc.authproxy import AuthServiceProxy
from docker import Client

#Variables and stuff
nudir = expanduser("~") + "/.nuTESTING"
dockercli = Client(base_url='unix://var/run/docker.sock',version='1.17')

def removenudir():
	shutil.rmtree(nudir)
	
def createnudir():
	if not os.path.exists(nudir):
		os.makedirs(nudir)

def createnuconf(content):
	createnudir()
	nuconf = nudir + "/nu.conf"
	
	with open(nuconf, 'w') as file_:
		file_.write(content)

def runcommand(command):
	
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = proc.communicate()
	
	return output

#get list of containers with the name format nunode#
def getnodes():
	
	containers = dockercli.containers(all=True)
		
	nodelist = []
	
	for node in containers:
		for name in node['Names']:
			name = name.replace("/","")
			m = re.match("^nunode[0-9]\d*$", name)
		
		if m:
			nodelist.append(name)
			
	nodelist.append("gui")
	return nodelist
	
def getprotocolport(nodename):
	if nodename == "gui":
		return 7895
	else:
		#return dockercli.port(nodename, 7895)[0]['HostPort']
		return runcommand("docker port %s 7895" % nodename)

#find unit RPC port for nodes
def getunitport(nodename, unit):
	unit = unit.lower()
	nodename = nodename.lower()
	
	if nodename == "gui":
		if unit == "s":
			return "15001"
		if unit == "b":
			return "15002"
	else:
		if unit == "s":
			#return dockercli.port(nodename, 15001)[0]['HostPort']
			return runcommand("docker port %s 15001" % nodename)
		if unit == "b":
			#return dockercli.port(nodename, 15002)[0]['HostPort']
			return runcommand("docker port %s 15002" % nodename)

#run RPC commands against gui and docker containers
class node():
	
	def __init__(self, nodename):
		rpc_user = 'user'
		rpc_password = 'pass'
		
		self.rpcs = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + (getunitport(nodename,"s")))
		self.rpcb = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + (getunitport(nodename,"b")))


#Create a dictionary called nodelist that generates and instance of the node class for each node.
#Then we can call each instance of the class by nodename
nodelist = {}

for nodename in getnodes():
	obj = node(nodename)
	
	nodelist[nodename] = obj

#addressbook get manage addresses for nodes. currently broken
class ab():
	def __init__(self):
		book = []
	
	def newaddress(self, nodename, unit):	
		if unit.lower() == "s":
			address = node(nodename).srpc.getnewaddress()
			#book.append({nodename : address})
		
		if unit.lower() == "b":
			#address = node(nodename).brpc.getnewaddress()
			book.append({nodename : address})
		
		return address
