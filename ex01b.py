import cv2
import numpy as np

img = cv2.imread('blackuni3.png')
print(img.shape)
img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
print(img2.shape)
cv2.imwrite('hoge.png', img2)

