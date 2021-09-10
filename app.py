from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        Link = request.form["link"]
        picture = request.form["url"]
        print(picture)
        return redirect(url_for("Link", Lk = Link))
    else:
        return render_template("upload.html")
    
@app.route("/<Lk>")
def Link(Lk):
    return f"<h1>{Lk}</h1>"


if __name__ == '__main__':
    app.run(debug = True)