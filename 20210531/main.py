from flask import Flask, render_template, request
import cv2
# opencv-python
# numpy
# flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    image = request.files['file']
    image.save(f"static/{image.filename}")
    print(image.filename)

    npimage = cv2.imread(f"static/{image.filename}")
    # npimage[0:100,0:100] = [0,0,0]
    roi = npimage[50:200,200:350]
    npimage[0:150,0:150] = roi
    npimage[:,:,2] = 0

    npimagename = f"static/np{image.filename}"
    cv2.imwrite(npimagename,npimage) #numpy 배열에 이미지화저장

    return render_template("print.html"\
       ,image=image.filename,npimage=npimagename)

app.run(host="127.0.0.1", port=5000);