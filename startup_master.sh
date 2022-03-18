#!/bin/bash

# a) Copy this file into ~ wget https://raw.githubusercontent.com/derekchased/se.uu.de1.project/master/startup_master.sh
# b) Change permissions of this file chmod u+x startup_master.sh
# c) Run this script ./startup_master.sh

# Move into reddit if not already there

cd reddit;

# 1. Init and pull from git

git init;

git remote add origin https://github.com/derekchased/se.uu.de1.project.git;

git pull origin master;

# 2. Create Swarm Cluster

sudo docker swarm init

# 3. Use the token provided here to add swarm nodes.

# 4. Get list of nodes

sudo node ls

# 5. Label docker nodes - Do this manually using container ids
# sudo docker node update --label-add node=sparkmaster <CONTAINER ID of master node>
# sudo docker node update --label-add node=sparkworker <CONTAINER ID OF worker node> 

# 6. Deploy stack to swarm - Do this manually when everything is ready

# sudo docker stack deploy -c <COMPOSE FILE docker-compose.yml> <APP NAMEsparkapp>
