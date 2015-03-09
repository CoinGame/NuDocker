#!/usr/bin/env python 

import simplejson as json
from bitcoinrpc.authproxy import AuthServiceProxy
from docker import Client
import random

#script, nodename = sys.argv


dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')
rpc_user = 'user'
rpc_password = 'pass'
node_name = 'node1'

rpcnsr = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + ((dockercli.port(node_name, 15001))[0]['HostPort']))
rpcnbt = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + ((dockercli.port(node_name, 15002))[0]['HostPort']))

rpcnsrgui = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:15001")
rpcnbtgui = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:15002")

def votecustodian():

#get a new NBT address to vote as custodian
 custaddr = rpcnbtgui.getnewaddress()
 rpcnsrgui.setvote({"parkrates":[],"custodians":[{"amount":1000000.0,"address":custaddr}],"motions":[],"fees":{}})


def sendnbt(to,amount="!"):
 if to == "docker":
  sendaddr = rpcnbt.getnewaddress()
  balance = rpcnbtgui.getbalance()
  if amount == "!":
   amount = random.uniform(.02,float(balance)*.01)
  print "Sending %r NBT to docker" % amount
  rpcnbtgui.sendtoaddress("%s" % sendaddr,amount)
 if to == "gui":
  sendaddr = rpcnbtgui.getnewaddress()
  balance = rpcnbt.getbalance()
  if amount == "!":
   amount = random.uniform(.02,float(balance)*.01)
  print "Sending %r NBT to gui" % amount
  rpcnbt.sendtoaddress("%s" % sendaddr,amount)
 
def sendnsr(to,amount="!"):
 if to == "docker":
  sendaddr = rpcnsr.getnewaddress()
  balance = rpcnsrgui.getbalance()
  if amount == "!":
   amount = random.uniform(.02,float(balance)*.01) 
  print "Sending %r NSR to docker" % amount
  rpcnsrgui.sendtoaddress("%s" % sendaddr,amount)
 if to == "gui":
  sendaddr = rpcnsrgui.getnewaddress()
  balance = rpcnsr.getbalance()
  if amount == "!":
   amount = random.uniform(.02,float(balance)*.01) 
  print "Sending %r NSR to gui" % amount
  rpcnsr.sendtoaddress("%s" % sendaddr,amount)





