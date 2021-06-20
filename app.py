from flask import Flask
import json

app = Flask(__name__)

# @app.route("")
# def home():
#     return "Hello! Main. <h1> inline html </h1>"


@app.route("/")
def home():
    # returning some set of JSON.
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    return y["city"]


if __name__ == "__main__":
    app.run()
