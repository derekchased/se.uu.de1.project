#!/bin/bash

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
# sudo mount <PATH TO VOLUME /dev/vdb> ./volume
























## Copy docker compose file from VM volume snapshot into reddit app directory

# cp <VOLUME PATH/docker-compose.yml> reddit

## Make data directory docker volume bind

mkdir data;

## Copy reddit files from VM volume snapshot into reddit directory data directory docker volume bind

# cp <VOLUME PATH/*> reddit/data


## A) Start Swarm Manager

# docker swarm init

# docker swarm init --advertise-addr <IP ADDRESS OF MANAGER NODE>
# docker swarm init --advertise-addr 130.238.28.102

## Check docker
# docker info
# docker node ls

## B) Add Swarm Nodes, run this command on each VM worker

# this is from the output when we create the manager
# docker swarm join --token <token>

# you can also get this link if you lose it running 
# docker swarm join-token worker

## Label docker nodes

# docker node update --addlabel <container id of master node> "sparkmaster"
# docker node update --addlabel <container id of all worker nodes> "sparkworker"

## Deploy stack to swarm 

# docker stack deploy -c 
