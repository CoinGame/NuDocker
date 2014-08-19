mkdir /root/.nu

touch /root/nu.conf

cd /root/.nu

echo testnet=1 > nu.conf
echo rpcuser=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >> nu.conf
echo rpcpassword=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >> nu.conf

cp nu.conf /nu.conf
