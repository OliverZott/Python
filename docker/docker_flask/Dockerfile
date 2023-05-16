FROM python:alpine

RUN echo "Dockerfile creating started... "

WORKDIR /FlaskStarTrek

COPY . .

RUN python -m venv venv
RUN pip install --no-cache-dir --upgrade -r env.txt

ENTRYPOINT [ "python"]
CMD ["app.py"]