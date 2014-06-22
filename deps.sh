#!/bin/bash
#Install Berkeley Database
cd /
mkdir db-4.8.30.nc
cd db-4.8.30.nc
wget http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
tar -xzvf db-4.8.30.NC.tar.gz
cd db-4.8.30.NC/build_unix
../dist/configure --enable-cxx
make
sudo make install
sudo ln -s /usr/local/BerkeleyDB.4.8/lib/libdb-4.8.so /usr/lib/libdb-4.8.so
sudo ln -s /usr/local/BerkeleyDB.4.8/lib/libdb_cxx-4.8.so /usr/lib/libdb_cxx-4.8.so
     
#Install Mini-UPnPC
cd /
mkdir miniupnpc
cd miniupnpc
wget "http://miniupnp.tuxfamily.org/files/miniupnpc-1.9.tar.gz"
tar -zxvf miniupnpc-1.9.tar.gz
cd miniupnpc-1.9/
sudo make install

cd /
