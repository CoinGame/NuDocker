#!/bin/bash
#Clone Peershares repo and compile deamon
cd ~/
echo "Cloning repo ..."
git clone https://github.com/peershares/peershares.git
cd peershares/src/
echo "Compiling source ..."
make -f makefile.unix BDB_INCLUDE_PATH="/usr/local/BerkeleyDB.4.8/include" BDB_LIB_PATH="/usr/local/BerkeleyDB.4.8/lib"
echo "Starting deamon ..."
./peersharesd
sleep 10
watch -n 30 ./peersharesd getinfo
