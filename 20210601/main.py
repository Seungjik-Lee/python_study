from flask import Flask,render_template,request
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/imgprint",methods=["POST","GET"])
def imgprint():
    file = request.files['file']
    filename = f"static/{file.filename}"
    file.save(filename)

    img = cv2.imread(filename)
    img[100:200,100:200] = [0,0,0]
    img[200:250,200:250] = [255,255,255]
    ar = img[50:100,50:100]
    img[0:50,0:50] = ar
    chfile = f"static/np{file.filename}"
    cv2.imwrite(chfile,img)

    img1 = cv2.imread(filename)
    expand = cv2.resize(img1,None,fx=1.3,fy=1.3,interpolation=cv2.INTER_CUBIC)
    exfile = f"static/ex{file.filename}"
    cv2.imwrite(exfile,expand)

    img1 = cv2.imread(filename)
    shri = cv2.resize(img1, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    shfile = f"static/sh{file.filename}"
    cv2.imwrite(shfile, shri)

    img1 = cv2.imread(filename)
    m = np.float32([[1,0,50],[0,1,100]])
    mimg = cv2.warpAffine(img1,m,(300,300))
    mfile = f"static/im{file.filename}"
    cv2.imwrite(mfile,mimg)

    img1 = cv2.imread(filename)
    m = cv2.getRotationMatrix2D((150,150),90,0.5)
    animg = cv2.warpAffine(img1,m,(300,300))
    anfile = f"static/an{file.filename}"
    cv2.imwrite(anfile,animg)

    return render_template("print.html", orifile=filename, chfile=chfile, exfile=exfile, shfile=shfile, mfile=mfile, anfile=anfile)

app.run(host="127.0.0.1",port="5001")