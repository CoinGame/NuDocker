#!/usr/bin/env python 

from bitcoinrpc.authproxy import AuthServiceProxy
from docker import Client


dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')
rpc_user = 'user'
rpc_password = 'pass'

nsrport = ((dockercli.port('node1', 15001))[0]['HostPort'])
nbtport = ((dockercli.port('node1', 15002))[0]['HostPort'])

accessNSR = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + nsrport)
accessNBT = AuthServiceProxy("http://" + rpc_user + ":" + rpc_password + "@127.0.0.1:" + nbtport)

print(accessNBT.getinfo())

