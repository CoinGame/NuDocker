Clone NuDocker and Nubit to your home directory. 

ex. 

~/NuDocker 

~/Nubit

**Running ABBAD.sh is optional. You can skip this step and move onto running StartContainer.sh if you copy your own version of the Nu daemon (nud) to the NuDocker folder first**

Use ABBAD.sh to generate a unique blockchain by pointing to the master source files. This will prevent clients from syncing up with the wrong chain or possibly the actual mainnet/testnet. Provide the path to source as a parameter. Make sure to use a full path.

ex. 

./ABBAD.sh ~/<Path to nubit source>


This script will generate the qt/daemon and copy the daemon to the NuDocker folder.

Then run StartContainer from the NuDcoker folder.

ex.

./StartContainer.sh

This will probably take a while if it's the first time you're running it. It should take a couple of seconds each time you run it after that unless you change the DockerFile. It it will download the Ubuntu 14.04 docker image, install the needed dependencies to run the daemon and some other stuff like nano and an ssh server.


It will automatically start three containers. You can edit this file if you would like to add more or remove some. You don't have to use all of them anyway. Once the script is completed it will automatically run (sudo docker ps) to show information about the containers. You will see five entries like this for each container.

0.0.0.0:49667->22/tcp

These show the port bindings to access resources inside the container. Docker works by binding one of the host ports and then forwarding it to the associated internal container port. In the example above the host port 49667 will connect us to port 22 inside the container. **You will have to ssh into the container and start nud before you can connect from the host.** ssh into the container like you would any server by using the host port binding.

ex.

ssh root@127.0.0.01 -p 49667

note that in any case where you're telling resources to access these ports you will use 127.0.0.1 instead of the displayed 0.0.0.0. **the default root password is "nubits".**

when you ssh into the container nud should be in the working directory. Just type ./nud --deamon and you should be ready to connect your container to the host. A testnet conf file will be automatically generated inside the container. We must prepare our host conf file to connect to the containers first.

Use the sample host conf file in the NuDocker folder to connect to your containers. You will see a section with the connect configuration parameter. All you need to do is replace PORT at the end of the connect parameter with the proper protocol port you will be using (either testnet port or mainnet port - they are both listed at the top of the file)

When you start the host's daemon/client it should connect to the containers that you listed in the conf file (as long as you started the daemon in the container as well)