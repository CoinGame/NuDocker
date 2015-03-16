#!/usr/bin/env python 

from docker import Client
import subprocess

dockercli = Client(base_url='unix://var/run/docker.sock',version='1.12')

subprocess.call("sudo docker run --name \"node1\" -t -d -P nodes")

container = dockercli.create_container(image='nodes', name="node1",network_disabled='false')
container2 = dockercli.create_container(image='nodes', name="node2",network_disabled='false')

dockercli.start(container)
dockercli.start(container2)
