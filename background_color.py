import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255

#ret, thresh = cv2.threshold(img, 127, 255, 0)
image = cv2.imread("photo_02.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
image_color = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
image = cv2.drawContours(image_color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", image_color)
cv2.waitKey()
cv2.destroyAllWindows()