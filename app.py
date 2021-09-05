from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Status of App</h1>the app is working"


if __name__ == '__main__':
    app.run()