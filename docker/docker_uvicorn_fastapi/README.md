# Docker FastAPI / Uvicorn Example

[Youtube](https://www.youtube.com/watch?v=zkMRWDQV4Tg&t=119s)

[FastAPI & Docker](https://fastapi.tiangolo.com/deployment/docker/)

## libs

- uvicorn [(link)](https://www.uvicorn.org/): `pip install uvicorn`
- fastApi [(link)](https://fastapi.tiangolo.com/) `pip install fastapi`
- or both: `pip install "uvicorn[standard]"`

# Local Execution

## venv

- `python -m venv venv`
- `.\venv\Scripts\activate`
- `pip install --upgrade -r ./requirements.txt`

Select respective python interpreter in IDE !!

## run & test

- `cd .\youtube-arjancodes\docker-usage\`
- `python -m uvicorn main:app --host 0.0.0.0 --port 8080 --reload`  
  [(link)](https://stackoverflow.com/questions/64936440/python-uvicorn-the-term-uvicorn-is-not-recognized-as-the-name-of-a-cmdlet-f)
- server: `localhost:8080/channels/2`
- swagger: `http://localhost:8080/docs`

# Containerized Execution

## Docker

- [Docker Demon - Docker Engine](https://stackoverflow.com/questions/60527336/what-is-the-difference-between-docker-daemon-and-docker-engine)

- install docker and run docker daemon
- Create Dockerfile (for docker image)
- **Docker Image**: In folder of dockerfile: `docker build -t channel-api-example .`
  - -t ... tag for image-name
- **Docker Container**: `docker run -d --name channel-api -p 8080:80 channel-api-example`
  - -p local:docker
  - -d ... detached to "get terminal back"
- test: `localhost:8080` .. now working from container without local server instance

### Changes

#### Manually

- Stop and Delete container
- make changes to code
- build image (faster because some steps already ran) and run  contianer again

#### Automated - Docker Compose

- **custom run command** restart server automatically on file-change
- **sync** folder (*volume*) on machine with folder in container
- it uses dockerfile, but replaces commands with own (`command:`)

- `docker-compose up --build`
  - up ... for synchronizing and server start
  - --build ... to build container the first time

## Docker commands

- `docker image ls`
- `docker  ps` = `docker container ls`
- `docker ps -a` ...show all (also not running)
- `docker run name/id`
- `docker stop name/id`

- Remove container and image (remove container before image)
  - `docker container rm name/id` or `docker rm name/id`
  - `docker image rm name/id` or `docker rmi name/id`

- Stop all containers:
  - `docker container ls -aq` ... generates list of all containers
  - `docker container stop $(docker container ls -aq)`
