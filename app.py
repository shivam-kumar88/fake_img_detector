<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, render_template, redirect, request, url_for
>>>>>>> test

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
<<<<<<< HEAD
=======

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
>>>>>>> test





if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug = True)
=======
    app.run()
>>>>>>> 6e7f9012868085812efe0da3898b8ce5c1669598
