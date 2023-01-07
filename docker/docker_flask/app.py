import os
from flask import Flask, render_template

app = Flask(__name__)

# Set env var (in linux shell): "> export FLASK_APP_NAME=MrSpocksWebsite; python app.py"
# in docker image/container: "> docker run -e APP_NAME=Scotty image_name-name"
env_var_value = os.environ.get('FLASK_APP_NAME')

# for env_name, env_value in os.environ.items():
#     print("{0}: {1}".format(env_name, env_value))


@app.route("/")
def main():
    # return render_template('index.html', color="blue")
    return render_template('index.html', app_name=env_var_value)


@app.route("/hello")
def hello():
    return "<p>Hello, from my first docker app :)</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
