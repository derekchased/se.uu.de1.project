#!/bin/bash

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
# docker node update --addlabel <CONTAINER ID of master node> "sparkmaster"
# docker node update --addlabel <CONTAINER ID OF ALL WORKER NODES> "sparkworker"

# 6. Deploy stack to swarm - Do this manually when everything is ready

# docker stack deploy -c <COMPOSE FILE docker-compose.yml> <APP NAMEsparkapp>
