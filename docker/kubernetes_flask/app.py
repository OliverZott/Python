import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Set env var:
#   - Linux:    "export FLASK_APP_NAME=MrSpocksWebsite; python app.py"
#   - Windowes: "setx FLASK_APP_NAME MrSpocksSite" and check: "gci env:"

# in docker image/container: "> docker run -e APP_NAME=Scotty image_name-name"

env_var_value = os.environ.get('FLASK_APP_NAME')
print(env_var_value)

# for env_name, env_value in os.environ.items():
#     print("{0}: {1}".format(env_name, env_value))


@app.route("/")
def main():
    return render_template('index.html', app_name=env_var_value)


@app.route("/hello")
def hello():
    return json.dumps({"name": env_var_value})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
