# simple-end-to-end-connection-docker
simple-end-to-end-connection-docker-with-prometheus

##build image
```docker build -t service1 .
```

```docker build -t service2 .
```

##deploy with swarm
```docker stack deploy -c docker-compose.yaml testing
```

##deploy monitoring
``` docker-compose up -d
```