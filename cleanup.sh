# /!bin/bash
sudo rm -rf ./srv/
docker ps -qa | xargs docker rm $1 --force
docker volume prune
echo "Everything is cleaned up"