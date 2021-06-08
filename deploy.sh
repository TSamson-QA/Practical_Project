#!/bin/bash

project_name=character_generator

# Build Server
docker build -t ${project_name}_server server

# Build class_api
docker build -t class_api class_api 

# Build race_api
docker build -t race_api race_api 

# Create Network
docker network create ${project_name}_network 

# Run containers
docker run -d -p 5000:5000 \
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    --name class_api \
    --network ${project_name}_network \
    class_api

docker run -d  \
    --name race_api \
    --network ${project_name}_network \
    race_api
