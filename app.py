from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return "<h1>Upload file</h1>you can upload your filr here"
    

if __name__ == '__main__':
    app.run()