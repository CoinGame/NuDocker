#!/bin/bash
#Clone Peershares repo and compile deamon
cd ~/
git clone https://github.com/peershares/peershares.git
cd peershares/src/
make -f makefile.unix BDB_INCLUDE_PATH="/usr/local/BerkeleyDB.4.8/include" BDB_LIB_PATH="/usr/local/BerkeleyDB.4.8/lib"
./peersharesd &
sleep 5
./peersharesd getinfo
./peersharesd getaddressesbyaccount ''
./peersharesd stop
