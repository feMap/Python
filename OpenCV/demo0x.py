# -*- coding: utf-8 -*-
import cv2
from cv2 import cv
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("building.jpg", cv2.IMREAD_GRAYSCALE)

# cv2.imshow("demo1", img)
# cv2.waitKey(0)

img_binary = cv2.Canny(img, 100, 255)
  
# cv2.imshow("demo1", img_binary)
# cv2.waitKey(0)

lines = cv2.HoughLinesP(img_binary, rho=1, theta=np.deg2rad(0.1),
                        threshold=96, minLineLength=33,
                        maxLineGap=4)

fig, ax = plt.subplots(figsize=(8, 6))
plt.imshow(img, cmap="gray")

from matplotlib.collections import LineCollection
lc = LineCollection(lines.reshape(-1, 2, 2))
ax.add_collection(lc)
ax.axis("off")

# plt.show()

img = cv2.imread("coins.jpg", cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (0, 0), 3)

###
cv2.imshow("demox", img_blur)
cv2.waitKey(6)
# assert None

circles = cv2.HoughCircles(img_blur, cv.CV_HOUGH_GRADIENT, dp=2.0, minDist=20.0,
                            param1=170, param2=44, minRadius=50, maxRadius=100)
 
print circles
x, y, r = circles[0].T

fig, ax = plt.subplots(figsize=(8, 6))
plt.imshow(img, cmap="gray")

from matplotlib.collections import EllipseCollection
ec = EllipseCollection(widths=2*r, heights=2*r, angles=0, units="xy",
                       facecolors="none", edgecolors="red",
                       transOffset=ax.transData, offsets=np.c_[x,y])
ax.add_collection(ec)
ax.axis("off")

plt.show()

