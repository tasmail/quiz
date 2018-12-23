# Quiz

An API server to manage Quiz project

## Howto

### Build docker container

```sh
cd docker
sudo ./build.sh 0.1.0
# 0.1.0 is a tag of container
sudo docker login
sudo docker push tas/quiz:TAG
```

### Run docker container
```sh
sudo docker run \
     --name quiz.host.com \
     -e SETTINGS="settings.production" \
     -e VIRTUAL_PORT=8283 \
     -e VIRTUAL_HOST="quiz.host.com" \
     --link mysql \
     -v /var/lib/quiz/quiz.host.com/var/log/quiz:/var/log/quiz \
     -v /var/lib/quiz/quiz.host.com/var/lib/quiz:/var/lib/quiz \
     -v /var/lib/quiz/quiz.host.com/opt/quiz:/opt/quiz \
     -td \
     tas/quiz:0.1.0
```
