# Kiwi.ki 
# SRE Task - Application 

- [x] Part1 - Create a simple backend application which will store a counter of pings from users
- [x] Part2 - Automate the deployment of the app created in part1. 

Usage | Tech
------|------
Web app |Python 3.5 + Flask 
Value Storage | Redis
LoadBalancing | HAproxy

# Usage
**Installation**
>The instructions assume that you have already installed [Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/). 

```bash
  git clone https://github.com/avenetj/kiwi.git .
```
**Part 1** 

> You must be root to use docker-compose commands and the docker deamon must be running

```bash
  cd part1/app
  docker-compose up -d --build
 ```
The web application should be available on : http://127.0.0.1:5000/ping

```bash
  curl 127.0.0.1:5000/ping
  curl 127.0.0.1:5000/total
```


The following URL are implemented
- /ping : increments the number of ping
- /total : displays the total number of ping
- /reset : resets the value stored to 0 

Shut down the application by running 
```bash
  docker-compose down 
```


**Part 2**
```bash
  cd ../../part2/app
  docker-compose up --build -d --scale app=2
```
The web application should be available on : http://127.0.0.1/ping (no need for the port)
The **--scale app=2** runs 2 app containers. You can change the value to adjust your needs. 

The same URL as before are implemented. 

```bash
  curl 127.0.0.1/ping
  curl 127.0.0.1/ping
  curl 127.0.0.1/total
```

You should get two differents hostname (container name) when doing the curl commands.  

Once you are done with the application, run this command to shut it down.
```bash
  docker-compose down 
```

Enjoy :octocat:
