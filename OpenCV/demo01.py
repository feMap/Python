# -*- coding: utf-8 -*-
import cv2
from cv2 import cv

filename = "lena.jpg"
img = cv2.imread(filename)

# 显示img的信息
print type(img), img.shape, img.dtype

# 修改成灰色照片 -- 将三维数组转化为二维数组
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print img_gray.shape

cv2.namedWindow("demo1")
cv2.imshow("demo1", img_gray)
cv2.waitKey(0)
