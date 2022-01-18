"""Erencan Güneş 160316023
   Abdüssamed Güzey 160316042"""

import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

process_list = [("+", 128), ("-", 128), ("*", 2), ("/", 2),("negative",0)]
img_list = os.listdir("imgs")


def transform(img, procedure=None):
    x = np.arange(0, 255, 1)
    if procedure == "+":
        y = x + 128
        for i in range(0, len(y)):
            if y[i] > 255:
                y[i] = 255
        return cv2.add(img, 128), y
    if procedure == "-":
        y = x - 128
        for i in range(0, len(y)):
            if y[i] < 0:
                y[i] = 0
        return cv2.subtract(img, 128), y
    if procedure == "*":
        y = x * 2
        for i in range(0, len(y)):
            if y[i] > 255:
                y[i] = 255
        return cv2.multiply(img, 2), y
    if procedure == "/":
        img = img / 2
        y = x / 2

        return cv2.divide(img, 2), y
    if procedure == "negative":
        y = 255 - x
        return cv2.bitwise_not(img),y

plt.figure(1)
for i in img_list:
    full_path = "imgs/" + str(i)
    img = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
    for k in process_list:
        t_img, y = transform(img, k[0])
        b = "i" + k[0] + str(k[1])
        print(img.shape)
        plt.subplot(231)
        plt.title("original")
        plt.imshow(img, "gray")

        plt.subplot(232)
        x = np.arange(0, 255, 1)
        plt.title("Transformation function  " + b)
        plt.plot(x, y)

        plt.subplot(233)

        plt.title(b)
        plt.imshow(t_img, "gray")

        plt.subplot(234)
        plt.title("original histogram")
        plt.hist(img.ravel(), 256, [0, 256])

        plt.subplot(235)
        ann = """
                Original min = {}
                Original max = {}
                Original mean = {}
                
                Modified min = {}
                Modified max = {}
                Modified mean = {}
        """.format(np.min(img), np.max(img), np.mean(img),
                   np.min(t_img), np.max(t_img), np.mean(t_img))

        plt.annotate(ann, (0, 0), xycoords="axes points")

        plt.subplot(236)
        plt.title("Modified histogram")
        plt.hist(t_img.ravel(), 256, [0, 256])

        plt.show()

        plt.clf()
