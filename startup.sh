#!/bin/bash

# a) Copy this file into ~
# b) Change permissions of this file chmod u+x startup.sh
# c) Run this script ./startup.sh

# 1. Update VM

sudo apt update;

sudo apt -y upgrade;

 # 2. Install Docker

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y;

curl -fsSL https://download.docker.com/linux/ubuntu/gpg |sudo apt-key add -;

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable";

sudo apt-get update;

sudo apt install docker-ce -y;

sudo apt install docker-compose -y;

# 3. Config docker launch on reboot

sudo systemctl enable docker.service;

sudo systemctl enable containerd.service;

# 4. Make data directory for reddit app 

mkdir reddit;

cd reddit;

# 5. Make volume directory

mkdir volume

# 6. Mount volume - Do this manually using correct path to volume
# sudo lsblk -f
# sudo mount <PATH TO VOLUME /dev/vdb> ./volume