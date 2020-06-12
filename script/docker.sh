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

docker service update --force --update-parallelism 1 --update-delay 30s --image oskar951/service1 oskar951/service1
docker service update --force --update-parallelism 1 --update-delay 30s --image oskar951/service2 oskar951/service2
docker service update --force --update-parallelism 1 --update-delay 30s --image oskar951/service3 oskar951/service3
docker service update --force --update-parallelism 1 --update-delay 30s --image oskar951/service4 oskar951/service4
docker service update --force --update-parallelism 1 --update-delay 30s --image oskar951/nginxservice oskar951/nginxservice

docker restart $(docker ps -a -q)

