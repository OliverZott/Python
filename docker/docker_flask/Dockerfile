FROM ubuntu

RUN echo 'Dockerfile first try =)'

RUN apt update
RUN apt -y install python3 python3.10-venv pip 

# RUN apt -y install git
# RUN git clone https://github.com/OliverZott/docker-examples.git

# COPY ./env.txt /FlaskExample

# changes dir for subsequent instructions!
WORKDIR /FlaskExample/ 

# Copy all files from current dir to docker-workdir
COPY . .

RUN python3 -m venv venv
RUN pip install --no-cache-dir --upgrade -r env.txt


# Start app:
# - version 1
# ENTRYPOINT FLASK_APP="app.py" flask run --host=0.0.0.0

# - version 2
ENTRYPOINT [ "python3" ]
CMD ["app.py" ]