FROM python:alpine

RUN echo "Dockerfile creating started... "

WORKDIR /FlaskStarTrek

COPY . .

RUN python -m venv venv
RUN pip install --no-cache-dir --upgrade -r env.txt

EXPOSE 8080

ENTRYPOINT [ "python"]
CMD ["app.py"]