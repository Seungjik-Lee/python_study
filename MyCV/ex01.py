import cv2

def doA():
    myimg = cv2.imread("ka.png")
    cv2.imshow("img",myimg)
    a = cv2.waitKey(0)  # 0은 무한정 기다릴때 쓰는거
    print('a = ',a)

    grayimg = cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gryimg",grayimg)
    b = cv2.waitKey(0)
    print('b = ',b)