import cv2

def doA():
    ka = cv2.imread("ka.png")
    cv2.imshow("ka", ka)
    cv2.waitKey(0)

    # roi = ka[0:200,0:200]
    # print(roi)
    # cv2.imshow("roi", roi)
    # cv2.waitKey(0)

    bgrv = ka[100,100]
    print(bgrv)