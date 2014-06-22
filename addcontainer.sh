#!/bin/bash
UNUMBER=1
USERNAME=testuser$UNUMBER
USEREXISTS=true
USERPASSWD=12345678

until [ "$USEREXISTS" = false ]; do
	if id -u $USERNAME >/dev/null 2>&1; then
		echo $USERNAME "exists"
		UNUMBER=$((UNUMBER+1))
		USERNAME=testuser$UNUMBER
	else
		echo $USERNAME "does not exist ... creating"
		USEREXISTS=false
	fi
done

useradd -m -p $USERPASSWD $USERNAME
usermod -a -G sudo $USERNAME
echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
mkdir /home/$USERNAME/.peershares
cp /peer-qa-containers/startdeamon.sh /home/$USERNAME
cp /peer-qa-containers/peershares.conf /home/$USERNAME/.peershares
cp -r /miniupnpc /home/$USERNAME
su - $USERNAME -c "sudo sh startdeamon.sh"
