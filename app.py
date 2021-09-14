
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

ssim = 1

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        Name = request.form["name"]
        link1 = request.form["imageup1"]
        
        link2 = request.form["imageup2"]
        print("link of picture 1: ", link1)
        print("linkof picture 2: ", link2)

            #requesting the link on web for content
        ige1 = requests.get(link1)
        ige2 = requests.get(link2)

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

        ig1_resize = ig1.resize((250,150))
        ig2_resize = ig2.resize((250,150))

        ig1_resize.save(r"D:\flask projects\fake_image_detector\resorse_image\images\img1_resized.png")
        ig2_resize.save(r"D:\flask projects\fake_image_detector\resorse_image\images\img2_resized.png")

        image_1 = cv2.imread(r"D:\flask projects\fake_image_detector\resorse_image\images\img1_resized.png")
        image_2 = cv2.imread(r"D:\flask projects\fake_image_detector\resorse_image\images\img2_resized.png")

        image_1_gray = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
        image_2_gray = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

        print("image-1 = ", image_1_gray)
        print("image-2 - ", image_2_gray)

        (score, diff) = structural_similarity(image_1_gray, image_2_gray, full=True)
        ssim_per = score*100
        print(ssim_per)
        global ssim
        ssim= ssim_per

        return redirect(url_for("Link", Lk = Name))
    else:
        return render_template("upload.html")

    
@app.route("/<Lk>")
def Link(Lk):
    #return f"<h1>{Lk}</h1>"
    return render_template(
        "up_suc.html",
        Lk = Lk,
        ssim_s = ssim)



if __name__ == '__main__':
    app.run(debug = True)
