
from flask import Flask, render_template, redirect, request, url_for
from PIL import Image
import pandas as pd
import os
import requests
import cv2
from skimage.metrics import structural_similarity
import imutils
from io import BytesIO



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        Name = request.form["name"]
        link1 = request.form["imageup1"]
        
        link2 = request.form["imageup2"]
        print("link of picture 1: ", link1)
        print("linkof picture 2: ", link2)

            #requesting the link on web for content
        ige1 = requests.get('https://images.unsplash.com/photo-1631465416799-02880b27977e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80')
        ige2 = requests.get('https://images.unsplash.com/photo-1631465416799-02880b27977e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80')

            #getting the content of the page
        ig1 = Image.open(BytesIO(ige1.content))
        ig2 = Image.open(BytesIO(ige2.content))

        #saving the image content to a given directory
        ig1.save(r"D:\flask projects\fake_image_detector\resorse_image\test_img1.png")
        ig2.save(r"D:\flask projects\fake_image_detector\resorse_image\test_img2.png")

        #getting size of the images
        ig1_size = ig1.size
        ig2_size = ig2.size
        print(ig1_size)
        print(ig1_size)

        return redirect(url_for("Link", Lk = Name))
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
