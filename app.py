
from flask import Flask, render_template, redirect, request, url_for
from PIL import Image

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        Link = request.form["link"]
        idelpicture = request.form["imageup1"]
        up1 = Image.open(idelpicture)
        print("idel image : ",idelpicture.format)
        picture_check = request.form["imageup2"]
        up2 = Image.open(picture_check)
        print("image to be checked : ",picture_check.format)
        return redirect(url_for("Link", Lk = Link))
    else:
        return render_template("upload.html")
    
@app.route("/<Lk>")
def Link(Lk):
    #return f"<h1>{Lk}</h1>"
    return render_template(
        "up_suc.html",
        Lk = Lk,)

if __name__ == '__main__':
    app.run(debug = True)
