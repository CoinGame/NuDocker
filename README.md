Clone NuDocker and Nubit source code

If you don't have the development dependencies installed run the dependencies script first to install all needed dependencies for scripts in this repo.


Use customizesource to generate a unique blockchain by pointing to the master source files. This will prevent your testing client from syncing up with the actual Nu mainnet/testnet. It also modifies the source to use a different data directory, so that you can test without impacting your actual main/test net data dir.  

Provide the path to source as a parameter. Make sure to use a full path. 

ex... ./customizesource ~/folder/nubit


This will take a while to run as it needs to build the daemon twice, and then the QT client. This script will generate the qt/daemon and copy them to the NuDocker folder.

Then run startcontainers from the NuDocker folder.

ex... ./startcontainers

This will probably take a while if it's the first time you're running it. It should take a couple of seconds each time you run it after that unless you change the DockerFile. It it will download the Ubuntu 14.04 docker image. It will start a single container called node1. When you run the Nu client in the NuDocker folder it will automatically connected to a deamon running in the docker contain and begin mining the first one billion shares. After it finishes mining restart the GUI and it will begin to mint.

You now have a two node NuNet running. askrpc.py can be used to communicate with the daemon running in the docker container.



