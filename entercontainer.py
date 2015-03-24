#!/usr/bin/env python 

#provide this script a container name as a parameter to enter inside it to bash terminal.

import os
import sys

script, nodename = sys.argv

os.system("docker exec -i -t %s /bin/bash" % nodename)
