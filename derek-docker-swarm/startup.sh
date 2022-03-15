
# Switch to root user

sudo bash;

### Update VM ###

apt update;

apt -y upgrade;

### Install Required Packages

apt install apt-transport-https ca-certificates curl software-properties-common -y;

### Install Docker ###

curl -fsSL https://download.docker.com/linux/ubuntu/gpg |sudo apt-key add -;

add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable";

apt-get update;

apt install docker-ce -y;

apt install docker-compose -y;

## Config docker launch on reboot

systemctl enable docker.service

systemctl enable containerd.service


## Make data directory for app 

mkdir reddit

## Make data directory docker volume bind

mkdir reddit/data

## Copy reddit files from VM volume snapshot into reddit directory data directory docker volume bind

cp <VOLUME PATH/*> reddit/data

# Clone github here??

mkdir g13;

cd g13;

# Build image

# docker build -t sparkaio/first:v0 .

## A) Start Swarm Manager
# expose ports

docker swarm init --advertise-addr <IP ADDRESS OF MANAGER NODE>
# docker swarm init --advertise-addr 130.238.28.102

## Check docker
# docker info
# docker node ls

## B) Add Swarm Nodes, run this command on each VM worker

# this is from the output when we create the manager
docker swarm join --token <token>

# you can also get this link if you lose it running 
# docker swarm join-token worker

## Label docker nodes

docker node update ...

## Deploy stack to swarm

docker stack deploy -c 
