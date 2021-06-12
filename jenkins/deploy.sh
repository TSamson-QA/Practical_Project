#!/bin/bash

#project_name=character_generator

#Copy over compose yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml 
#docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager "docker stack deploy --compose-file docker-compose.yaml character_generator"

# Build Server
#docker build -t ${project_name}_server server

# Build class_api
#docker build -t class_api class_api 

# Build race_api
#docker build -t race_api race_api

# Build alignment_api
#docker build -t alignment_api alignment_api 

# Create Network
#docker network create ${project_name}_network 

# Run containers
#docker run -d -p 5000:5000 \
 #   --name ${project_name}_server \
  #  --network ${project_name}_network \
   # ${project_name}_server

#docker run -d \
 #   --name class_api \
  #  --network ${project_name}_network \
   # class_api

#docker run -d  \
 #   --name race_api \
  #  --network ${project_name}_network \
   # race_api

#docker run -d  \
 #   --name alignment_api \
  #  --network ${project_name}_network \
   # alignment_api
