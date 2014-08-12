Clone NuDocker to your home directory. ex. ~/NuDocker

Use ABBAD.sh to generate a unique blockchain by pointing to the master source files. This will prevent clients from syncing up with the wrong chain or possibly the actual mainnet/testnet. Provide the path to source as a parameter.

ex. 

./ABBAD.sh ~/<Path to nubit source>


This script will generate the qt and daemon, and then copy the daemon to the NuDocker folder to place into containers when we create them. 


