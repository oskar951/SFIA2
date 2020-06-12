#!/bin/bash
source ~/.bashrc
#fix docker.sock permission denied
sudo chmod 666 /var/run/docker.sock

docker build -t oskar951/service1:latest ./service1
docker build -t oskar951/service2:latest ./service2
docker build -t oskar951/service3:latest ./service3
docker build -t oskar951/service4:latest ./service4
docker build -t oskar951/nginxservice:latest ./nginx

docker push oskar951/service1
docker push oskar951/service2
docker push oskar951/service3
docker push oskar951/service4
docker push oskar951/nginxservice



docker stack deploy --compose-file docker-compose.yaml stackdemo

docker restart $(docker ps -a -q)

