# RabbitMQ Examples

- <https://www.rabbitmq.com/tutorials/tutorial-one-python.html>

## Prerequisites

### docker

- `docker pull`

### curl (if using cli)

- `choco install curl`
  - If error: `Remove-item alias:curl`  ... remove wrong alias
- `choco install jq`  ... response formatter
- Usage e.g. `curl -u guest http://localhost:15672/api/vhosts | jq`

### venv

- create venv
- activte / deactivate venv
- install packages with activated env and check

```bash
python -m venv venv
.\venv\Scripts\deactivate
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install --upgrade -r ./environment/requirements.txt
pip list
```

or

- `python -m pip install -r ./environment/requirements.txt`

pika-stubs

- <https://github.com/hahow/pika-stubs>

## Run application

- Docker container
  - `docker start <containerid> -a`

      or

  - `docker run --rm -d -p 15672:15672 -p 5672:5672 --name my_rabbit rabbitmq:3-management`
      with `--hostname my-rabbit_db` for specific db name an `-it` for interactive mode after attaching
  - `docker attach <contianerId>`
  - `docker logs <containerid>`
  - `http://localhost:15672/`
  - API:
    - `http://localhost:15672/api/index.html`
    - `http://localhost:15672/api/queues`
    - `http://localhost:15672/api/connections`
- Start 2 terminals:
  - `python .\hello-world\send.py`
  - `python .\hello-world\receive.py`
