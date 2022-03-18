#!/bin/bash

# a) Copy this file into ~ wget https://raw.githubusercontent.com/derekchased/se.uu.de1.project/master/startup_worker.sh
# b) Change permissions of this file chmod u+x startup_worker.sh
# c) Run this script ./startup_worker.sh

# 1. Add this vm to the swarm cluster

# sudo docker swarm join --token <TOKEN FROM MASTER>