#!/usr/bin/env python 

import os
import re
import random
import shutil
import subprocess
import simplejson as json
from os.path import expanduser
from toolbox import *
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
		return dockercli.port(nodename, 7895)[0]['HostPort']

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
			return dockercli.port(nodename, 15001)[0]['HostPort']
		if unit == "b":
			return dockercli.port(nodename, 15002)[0]['HostPort']

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
		






#def getnewaddress (unit, source):
	#try:
		#if unit == "nsr":
			
		#if unit == "nbt":
			#if source == "docker":
				#return rpcnbt.getnewaddress()
			#if source == "gui":
				#return rpcnbtgui.getnewaddress()
	#except: pass

#class transaction(sender, recipient):

	#def __init__(self, sender, recipient):
		#sendaddr = self.sendaddr
		#recieveaddr = self.recieveaddr

	#def sendnbt(sendaddr, recieveaddr):
		#print "test"

#def votecustodian():
##get a new NBT address to vote as custodian
#custaddr = rpcnbtgui.getnewaddress()
#rpcnsrgui.setvote({"parkrates":[],"custodians":[{"amount":1000000.0,"address":custaddr}],"motions":[],"fees":{}})

#def sendnbt(to,amount="!"):
#if to == "docker":
	#sendaddr = rpcnbt.getnewaddress()
	#balance = rpcnbtgui.getbalance()
#if amount == "!":
	#amount = random.uniform(.02,float(balance)*.01)
	#print "Sending %r NBT to docker" % amount
	#rpcnbtgui.sendtoaddress("%s" % sendaddr,amount)
#if to == "gui":
	#sendaddr = rpcnbtgui.getnewaddress()
	#balance = rpcnbt.getbalance()
#if amount == "!":
	#amount = random.uniform(.02,float(balance)*.01)
	#print "Sending %r NBT to gui" % amount
	#rpcnbt.sendtoaddress("%s" % sendaddr,amount)
	
#def sendnsr(to,amount="!"):
#if to == "docker":
	#sendaddr = rpcnsr.getnewaddress()
	#balance = rpcnsrgui.getbalance()
#if amount == "!":
	#amount = random.uniform(.02,float(balance)*.01) 
	#print "Sending %r NSR to docker" % amount
	#rpcnsrgui.sendtoaddress("%s" % sendaddr,amount)
#if to == "gui":
	#sendaddr = rpcnsrgui.getnewaddress()
	#balance = rpcnsr.getbalance()
#if amount == "!":
	#amount = random.uniform(.02,float(balance)*.01) 
	#print "Sending %r NSR to gui" % amount
#rpcnsr.sendtoaddress("%s" % sendaddr,amount)
