import cv2

img = cv2.imread("static/gray_image.jpg", cv2.IMREAD_GRAYSCALE)

images = []

ret,thre1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret,thre2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret,thre3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret,thre4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret,thre5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

images.append(thre1)
images.append(thre2)
images.append(thre3)
images.append(thre4)
images.append(thre5)

# for index, img in enumerate(images):
#      cv2.imshow(str(index), img)
#      cv2.waitKey(0)

himg = cv2.imread("static/hand_writing_image.jpg", cv2.IMREAD_GRAYSCALE)

th1 = cv2.adaptiveThreshold(himg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)
th2 = cv2.adaptiveThreshold(himg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

images.append(th1)
images.append(th2)

for index, img in enumerate(images):
    cv2.imshow(str(index), img)
    cv2.waitKey(1000)

cv2.waitKey(0)