#!/bin/bash

project_name=character_generator

#Copy over compose yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml 
#docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager << EOF
    export DATABASE_URI=$(DATABASE_URI)
    docker stack deploy --compose-file docker-compose.yaml character_generator
EOF
# Build Server
docker build -t character_generator_server server

# Build class_api
docker build -t class_api class_api 

# Build race_api
docker build -t race_api race_api

# Build alignment_api
docker build -t alignment_api alignment_api 

# Create Network
docker network create character_generator_network 

# Run containers
docker run -d -p 5000:5000 \
    --name character_generator_server \
    --network character_generator_network \
    character_generator_server

docker run -d \
    --name class_api \
    --network character_generator_network \
    class_api

docker run -d  \
    --name race_api \
    --network character_generator_network \
    race_api

docker run -d --name alignment_api --network character_generator_network alignment_api
