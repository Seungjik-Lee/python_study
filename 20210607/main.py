from flask import Flask, request, render_template
import cv2
from pip._internal import req

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    print('file = ', file)
    oimg = f"static/{file.filename}"
    file.save(oimg)

    narr = cv2.imread(oimg)
    # print(narr.shape)
    height, width = narr.shape[:2]
    M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
    dstarr = cv2.warpAffine(narr, M, (width, height))
    dimg = f"static/m{file.filename}"
    cv2.imwrite(dimg, dstarr)
    return render_template("print.html", oimg=oimg, dimg=dimg)

@app.route("/addimg", methods=["POST"])
def upload():
    file1 = request.files['file1']
    file2 = request.files['file2']
    file1name = f"/static/{file1.filename}"
    file2name = f"/static/{file2.filename}"
    file1.save(file1name)
    file2.save(file2name)

    arr1 = cv2.imread(file1name)
    arr2 = cv2.imread(file2name)
    addcv2 = cv2.add(arr1,arr2)
    nparr3 = arr1+arr2
    cv2filename = "f/static/saimg"
    npfilename = "f/static/nimg"
    cv2.imwrite(cv2filename,addcv2)
    cv2.imwrite(npfilename,nparr3)
    return render_template("print1.html", cv2filename=cv2filename, npfilename=npfilename)

# 서버 실행... 사용자의 요청을 기다립니다.
app.run(host="127.0.0.1", port=5001, debug=True)
