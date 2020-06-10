#!/bin/bash

#fix docker.sock permission denied
sudo chmod 666 /var/run/docker.sock

docker stack deploy --compose-file docker-compose.yaml stackdemo