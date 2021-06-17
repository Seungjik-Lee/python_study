from flask import Flask, render_template
from alone2_1 import maketraintest
import cv2

img1 = cv2.imread("static/image_1.jpg")
img2 = cv2.imread("static/image_2.png")

img3 = cv2.add(img1, img2)
cv2.imshow()

app = Flask(__name__)

@app.route("/")
def index():
    maketraintest()
    return render_template("index.html")

app.run(host="127.0.0.1", port="5000")