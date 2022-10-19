# Work Queue

## Run example

- Start docker container:
  - `docker run --rm -d -p 15672:15672 -p 5672:5672 --name my_rabbit rabbitmq:3-management`

  or

  - `docker start <containerid> -a`
- Run sample app:
  - 3 Terminals
  - `python .\worker.py`
  - `python .\worker.py`
  - tasks:
    - `python .\new_task.py task.`
    - `python .\new_task.py task..`
    - `python .\new_task.py task...`
    - `python .\new_task.py task....`
    - `python .\new_task.py task.....`
