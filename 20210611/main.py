from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#flask 웹 모듈 라이브러리
#sklearn 알고리즘 라이브러리
#matplotlib 그래프 그려주는 라이브러리
#api
#웹 or 앱으로 보여줘야 고객이 씀


app = Flask(__name__)


@app.route("/")
def home():
    wlength = request.args.get("length",default=30, type=float) #데이터가 안들어오면 30으로 줘라
    wweight = request.args.get("weight", default=600, type=float) #데이터가 안들어오면 600으로 줘라
    # 도미 데이터
    bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0,
                    33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5,
                    39.5, 41.0, 41.0]
    bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0,
                    600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0,
                    850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]


    # 빙어 데이터
    smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
    smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

    plt.scatter(bream_length, bream_weight, marker='o') #도미 데이터 그리기
    plt.scatter(smelt_length, smelt_weight, marker='*') #빙어 데이터 그리기

    plt.scatter(wlength,wweight,marker='^')


    plt.xlabel('length')
    plt.ylabel('weight')
    brimg = f"static/brimg.png"
    plt.savefig(brimg)
    plt.close()

    length = bream_length+smelt_length # x 배열합치기
    weight = bream_weight+smelt_weight # y 배열합치기

    # 2차원 배열
    fish_data = [[l,w] for l,w in zip(length,weight)]
    print(fish_data)

    fish_target = [1]*35 + [0]*14
    print(fish_target)

    knc = KNeighborsClassifier() # 이웃된것을 보고 분류하는 클래스
    knc.fit(fish_data, fish_target) # 데이터 만든것 넣는 함수
    svalue = knc.score(fish_data, fish_target) # 이 데이터를 넣을 때 알고리즘 확률
    tvalue = knc.predict([[wlength,wweight]]) # 데이터를 넣을 때 1, 0 인지 판단하는 함수

    print('svalue',svalue)
    print('tvalue',tvalue)
    prevalue ="도미"
    if tvalue ==1:
        prevalue = "도미"
    else:
        prevalue = "빙어"

    #plt.show()

    return render_template("index.html", brimg=brimg, prevalue=prevalue)

app.run(host="127.0.0.1", port=5000)