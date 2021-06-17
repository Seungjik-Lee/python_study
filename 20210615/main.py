from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import cv2

img1 = cv2.imread("static/image_1.jpg")
img2 = cv2.imread("static/image_2.png")

img3 = cv2.add(img1, img2)
cv2.imshow("img3", img3)
cv2.waitKey(0)

img4 = np.add(img1, img2)
cv2.imshow("img4", img4)
cv2.waitKey(0)