#!/bin/bash

#########USAGE FOR AUTOBUILDBLOCKCHAIN #########
#You must provide the full path to the clone nubits repo as the first parameter
#You must update the variable values below this section with the values that are to be substituted into the source code

#EXAMPLE: sudo ABB.sh ~/<Nubits Repo Clone Dir>


#STATIC SOURCE VARS - This section is where you will put the existing values from the source. Meaning, The values that we are searching for in the code to replace
srcV3SwitchOfficial="unsigned int nProtocolV03SwitchTime"
srcV3SwitchTestnet="unsigned int nProtocolV03TestSwitchTime"
srcV4SwitchOfficial="unsigned int nProtocolV04SwitchTime"
srcV4SwitchTestnet="unsigned int nProtocolV04TestSwitchTime"
srcHashGenesisBlockOfficial="static const uint256 hashGenesisBlockOfficial("
srcHashGenesisBlockTestNet="static const uint256 hashGenesisBlockTestNet("
srcOfficialNonce="        unsigned int nNonceGenesis="
srcTestnetNonce="            nNonceGenesis="
srcTimeGenesisOfficial="        unsigned int nTimeGenesis="
srcTimeGenesisTestnet="            nTimeGenesis="
srcPszTimestampOfficial=" pszTimestamp = "
srcPszTimestampTestnet="            pszTimestamp="
srcMerkleRootOfficial="3e6c2608685f1d66d8fe9cb798400ec16aec1574b7ad9a7a92a65c7fcea2d32a"
srcMerkleRootTestNet="d044ad667adb2ec5073dc2f033f8ed9458f92515eb13310fb1fccfb4242cf31d"

#Seting some predefined variables to use later
RegularTimeSwitch=$(date --date='1 day'  --utc)
EpochTimeSwitch=$(date +%s --date='1 day')
RegularTime=$(date)
EpochTime=$(date +%s)
#Get a big ass random string
RandomString=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

if [[ $2 = "dep" ]]; then

#Install dependencies
sudo apt-add-repository ppa:bitcoin/bitcoin -y

sudo apt-get update
sudo apt-get install git build-essential g++ libssl-dev libboost-all-dev libdb4.8++-dev libqrencode-dev qt4-qmake libqt4-dev docker.io -y

#Needed to install docker
sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker
sudo sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io

#Install Mini-UPnPC
cd ~
mkdir miniupnpc
cd miniupnpc
wget "http://miniupnp.tuxfamily.org/files/download.php?file=miniupnpc-1.9.tar.gz"
tar -zxvf download.php?file=miniupnpc-1.9.tar.gz
cd miniupnpc-1.9/
sudo make install

fi #END INSTALLING DEPENDENCIES


#take in the location to the source as parameter"
src=$1/src
if [ -z "$1" ]; then 
echo "please provide path to folder as parameter" && exit 
fi #END PATH CHECK

#change working directory to source folder
cd "$src"

echo \##########################################
echo \########Creating New Genesis Block########
echo \##########################################
sed -i -e "s@$srcPszTimestampOfficial.*@ pszTimestamp = \"$RegularTime $RandomString\";@" \
-e "s@$srcPszTimestampTestnet.*@            pszTimestamp=\"$RegularTime $RandomString\";@" \
-e "s@$srcTimeGenesisOfficial.*@        unsigned int nTimeGenesis=$EpochTime;@" \
-e "s@$srcTimeGenesisTestnet.*@            nTimeGenesis=$EpochTime;@" \
-e "s@$srcOfficialNonce.*@        unsigned int nNonceGenesis=0;@" \
-e "s@$srcTestnetNonce.*@            nNonceGenesis=0;@" main.cpp

make -f makefile.unix

cd ~

#Create the conf file with the rpcuser and rpcpasswords set

rm -rf ~/.nu

cd ~
mkdir -p ~/.nu
cd ~/.nu
touch nu.conf
echo rpcuser=safasfasdf >> nu.conf
echo rpcpassword=asdfasdfadsf >> nu.conf

cd "$src"

./nud --daemon &

sleep 15

./nud --daemon --testnet &

sleep 15


#Parsing debug logs for needed strings
cd ~/.nu

#Genesis Hash
officialGenHash=$(cat debug.log | grep "genesis hash")
IFS='=' read -a OffGenHash <<< "$officialGenHash"
genHashString="${OffGenHash[1]}"

#Nonce
officialNonce=$(cat debug.log | grep "nNonce")
IFS=',' read -a OffNonce <<< "$officialNonce"
IFS='=' read -a OffNonce2 <<< "${OffNonce[6]}"
NonceString="${OffNonce2[1]}"

#Merkle Root
officialMerkleRoot=$(cat debug.log | grep "merkle root")
IFS='=' read -a OffMerkRoot <<< "$officialMerkleRoot"
merkRootString="${OffMerkRoot[1]}"

#Now let's parse the testnet debug!!

cd testnet

#Genesis Hash
testnetGenHash=$(cat debug.log | grep "genesis hash")
IFS='=' read -a testGenHash <<< "$testnetGenHash"
genHashStringTest="${testGenHash[1]}"

#Nonce
testnetNonce=$(cat debug.log | grep "nNonce")
IFS=',' read -a TestNonce <<< "$testnetNonce"
IFS='=' read -a TestNonce2 <<< "${TestNonce[6]}"
NonceStringTest="${TestNonce2[1]}"

#Merkle Root
testMerkleRoot=$(cat debug.log | grep "merkle root")
IFS='=' read -a TestMerkRoot <<< "$testMerkleRoot"
merkRootStringTest="${TestMerkRoot[1]}"

#Completed parsing debug - begin substitution

cd "$src"

sed -i -e "s@.*$srcV3SwitchOfficial.*@unsigned int nProtocolV03SwitchTime     = $EpochTimeSwitch; // $RegularTimeSwitch UTC@g" \
-e "s@.*$srcV3SwitchTestnet.*@unsigned int nProtocolV03TestSwitchTime     = $EpochTimeSwitch; // $RegularTimeSwitch UTC@g" \
-e "s@.*$srcV4SwitchOfficial.*@unsigned int nProtocolV04SwitchTime     = $EpochTimeSwitch; // $RegularTimeSwitch UTC@g" \
-e "s@.*$srcV4SwitchTestnet.*@unsigned int nProtocolV04TestSwitchTime = $EpochTimeSwitch; // $RegularTimeSwitch UTC@g" kernel.cpp

sed -i -e "s@.*$srcHashGenesisBlockOfficial.*@static const uint256 hashGenesisBlockOfficial(\"$genHashString\");@" \
-e "s@.*$srcHashGenesisBlockTestNet.*@static const uint256 hashGenesisBlockTestNet(\"$genHashStringTest\");@" main.h

sed -i -e "s@.*$srcPszTimestampOfficial.*@        const char* pszTimestamp = \"$RegularTime $RandomString\";@" \
-e "s@.*$srcPszTimestampTestnet.*@            pszTimestamp=\"$RegularTime $RandomString\";@" \
-e "s@.*$srcOfficialNonce.*@        unsigned int nNonceGenesis=$NonceString;@" \
-e "s@.*$srcTestnetNonce.*@            nNonceGenesis=$NonceStringTest;@" \
-e "s@.*$srcTimeGenesisOfficial.*@        unsigned int nTimeGenesis=$EpochTime;@" \
-e "s@.*$srcTimeGenesisTestnet.*@            nTimeGenesis=$EpochTime;@" \
-e "s@assert(block.hashMerkleRoot == uint256(\"0x$srcMerkleRootOfficial\"));@assert(block.hashMerkleRoot == uint256(\"0x$merkRootString\"));@" \
-e "s@assert(block.hashMerkleRoot == uint256(\"0x$srcMerkleRootTestNet\"));@assert(block.hashMerkleRoot == uint256(\"0x$merkRootStringTest\"));@" main.cpp


#need to fix this so i don't have to update the merkelroot when it changes. All other lines that need to be changed can be found dynamicaly.

#cat main.cpp | tr '\n' '@' | sed -e "s/"@$srcMerkleRootOfficial.*@"/            assert(block.hashMerkleRoot == uint256(\"0x$merkRootString\"));/1" \
#-e "s/@$srcMerkleRootTestNet.*@/            assert(block.hashMerkleRoot == uint256(\"0x$merkRootStringTest\"));/2" | tr '@' '\n' > main.cppp


make -f makefile.unix

cd ..

qmake

make

mv ~/.nu ~/.nu$RandomString
mkdir ~/.nu

cd ~/.nu
touch nu.conf

echo \#testnet=1 >> nu.conf
echo \#server=1 >> nu.conf
echo rpcuser=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >> nu.conf
echo rpcpassword=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >> nu.conf

echo \#INFO >> nu.conf
echo \#PROTOCOL PORT 7890 >> nu.conf
echo \#RPC PORT 14001 >> nu.conf
echo \#TESTNET PORT      7895 >> nu.conf
echo \#TESTNET RPC PORT 15001 >> nu.conf


echo "MerkleRoot=$merkRootString"
echo "GenHashString=$genHashString"
echo "NonceString=$NonceString"
echo "TestMerkleRoot=$merkRootStringTest"
echo "TestGenHashString=$genHashStringTest"
echo "TestNonceString=$NonceStringTest"


#BEGIN DOCKER SECTION

#Making sure we have the image we will use for our docker 

mkdir ~/nudocker
cd ~/nudocker

cp ~/nubit/src/nud ~/nudocker

#touch Dockerfile
#echo FROM phusion/baseimage >> Dockerfile

#echo RUN apt-add-repository ppa:bitcoin/bitcoin -y >> Dockerfile
#echo RUN apt-get update >> Dockerfile
#echo RUN apt-get install git build-essential g++ libssl-dev libboost-all-dev libdb4.8++-dev libqrencode-dev qt4-qmake libqt4-dev -y
#echo RUN ADD ./nud /tmp >> Dockerfile







