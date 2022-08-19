FROM python:latest

# set working dir inside container-filesystem
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
# dependencies before code, because docker can start from here if code is changed (dependencies stay the same)
COPY . /app

# start the server (internal port 80... default port inside container)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]