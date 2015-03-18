#!/usr/bin/env python 

import simplejson as json
import random
import re
from bitcoinrpc.authproxy import AuthServiceProxy
from docker import Client

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')
 
#get list of containers with the name format nunode#
def getnodes(listall=False):
	
	if listall == False:
		containers = dockercli.containers()
	
	if listall == True:
		containers = dockercli.containers(all=True)
		
	nodelist = []
	
	for node in containers:
		for name in node['Names']:
			name = name.replace("/","")
			m = re.match("^nunode[0-9]\d*$", name)
		
		if m:
			nodelist.append(name)
			
	return nodelist
	
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
		
		self.srpc = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + (getunitport(nodename,"s")))
		self.brpc = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + (getunitport(nodename,"b")))
		
class nodes(node):
	def __init__(self):
		
		lstnodes = getnodes()
		
		for i in lstnodes:
			self.node(i)
		
#addressbook get manage addresses for nodes.
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
