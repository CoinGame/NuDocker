#!/usr/bin/env python 

import simplejson as json
from bitcoinrpc.authproxy import AuthServiceProxy
from docker import Client
import random

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')
 
def getnodeport(nodename, unit):
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

class node(object):
	
	def __init__(self, nodename, unit):
		rpc_user = 'user'
		rpc_password = 'pass'
		self.rpc = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + (getnodeport(nodename,unit)))

class AddressBook(dict):
	def __init__(self):
		print "test"

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
