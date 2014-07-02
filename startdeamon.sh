#!/bin/bash
#Clone Peershares repo and compile deamon
cd ~/
cd nubit/src/
echo "Compiling source ..."
make -f makefile.unix BDB_INCLUDE_PATH="/usr/local/BerkeleyDB.4.8/include" BDB_LIB_PATH="/usr/local/BerkeleyDB.4.8/lib"
echo "Starting deamon ..."
./nud &
sleep 7
while true; do
./peersharesd getinfo
./peersharesd getaddressesbyaccount ''
sleep 30
done
