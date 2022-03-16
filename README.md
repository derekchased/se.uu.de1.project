# Data Engineering 1 Project Group 13



reddit
- docker-compose.yml
- app
reddit/app
- project.py
- data
reddit/app/data
- data files



## Instances

docker swarm join --token SWMTKN-1-5t5tgg1juzbx9sosad14ivdpt8gg4effnczb30f4jd1sela6e2-7eebp378nhp6um1jnsd3h9xve 130.238.29.153:2377

p_g13_1: 130.238.29.153
			container id: 1d5f9923626e
p_g13_2: 130.238.29.154
			container id: e8a84bae1823
p_g13_3: 130.238.29.77
			container id: d651412504cf


=======

1. ssh into machine
2. mkdir reddit
3. cd reddit
3. mkdir app
4. mkdir app/data
5. check, sudo lsblk -f
6. format, sudo mkfs.ext4 /dev/vdb
7. mount, sudo mount /dev/vdb ./volume

scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2011-08.bz2 ubuntu@130.238.29.153:/home/ubuntu/reddit/app/data
scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2011-08.bz2 ubuntu@130.238.29.154:/home/ubuntu/reddit/app/data
scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2011-08.bz2 ubuntu@130.238.29.77:/home/ubuntu/reddit/app/data



scp ~/www/se.uu/se.uu.de1.project/notebook/project.py ubuntu@130.238.29.77:/home/ubuntu/reddit/app
scp ~/www/se.uu/se.uu.de1.project/bitnami/docker-compose.yml ubuntu@130.238.29.77:/home/ubuntu/reddit



# login to a container
docker exec -it 1d5f9923626e /bin/bash
docker exec -it 1d5f9923626e spark-submit project.py

# copy file into a container
docker cp foo.txt container_id:/foo.txt

# run command on docker container from local machine
ssh -t ubuntu@130.238.29.153 sudo docker exec -it 1d5f9923626e spark-submit project.py




docker exec -it af3e3acef972 spark-submit --deploy-mode cluster reddit/project.py








====
130.238.29.184

scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2006-03.bz2 ubuntu@130.238.29.153:/home/ubuntu/reddit/volume

scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2007-03.bz2 ubuntu@130.238.29.153:/home/ubuntu/notebook

scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2009-05.bz2 ubuntu@130.238.29.153:/home/ubuntu/notebook


scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2006-03.bz2 ~/www/se.uu/se.uu.de1.project/notebook/RC_2007-03.bz2 ~/www/se.uu/se.uu.de1.project/notebook/RC_2009-05.bz2 ubuntu@130.238.29.184:/home/ubuntu/reddit/volume


scp ~/www/se.uu/se.uu.de1.project/notebook/RC_2017-11.bz2 ubuntu@130.238.29.184:/home/ubuntu/reddit/volume

scp ~/www/se.uu/se.uu.de1.project/bitnami/docker-compose.yml ubuntu@130.238.29.184:/home/ubuntu/reddit


rsync -r -v --progress -e ssh /Users/derek/www/se.uu/se.uu.de1.project/notebook/large ubuntu@130.238.29.184:/home/ubuntu/reddit/large