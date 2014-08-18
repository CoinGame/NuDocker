sudo apt-add-repository ppa:bitcoin/bitcoin -y

sudo apt-get update
sudo apt-get install git build-essential g++ libssl-dev libboost-all-dev libdb4.8++-dev libqrencode-dev qt4-qmake libqt4-dev wget -y

#Install Mini-UPnPC
cd ~
mkdir miniupnpc
cd miniupnpc
wget "http://miniupnp.tuxfamily.org/files/download.php?file=miniupnpc-1.9.tar.gz"
tar -zxvf download.php?file=miniupnpc-1.9.tar.gz
cd miniupnpc-1.9/
sudo make install
