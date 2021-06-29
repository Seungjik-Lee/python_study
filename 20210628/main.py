from flask import Flask, render_template, request  # 웹라이브러리
from graph import makeperch


app = Flask(__name__)


@app.route("/")
def home():
    length = request.args.get('length')
    if length is None:
        length = 50
    # print(length)
    perch,weight = makeperch(int(length))
    return render_template('3_3.html', perch=perch, weight=weight)


app.run(host="127.0.0.1", port=5000, debug=True)
