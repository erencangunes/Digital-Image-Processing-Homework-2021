"""Erencan Güneş 160316023
   Abdüssamed Güzey 160316042"""
   
import cv2
import numpy as np

img = cv2.imread("32.tif", 0)

code = np.mod(img, 2)

first = []

code = code.ravel()

k = 0
for a in range(0, 256):
    for i in range(0, len(code), 256):
        first.append(code[i + k])
    k += 1

first = np.array(first)
first = first.reshape((8192, 8))
binarr = []
for i in first:
    i = str(i)
    i = i.replace("[", "")
    i = i.replace("]", "")
    i = i.replace(" ", "")
    i = i.replace(".", "")
    binarr.append(i)

text = []
decarr = []
for i in binarr:
    decarr.append(int(i, 2))

for i in decarr:
    text.append(chr(i))

new_text = []
for i in text:
    new_text.append(i)
    if i == "%":
        break
text = ""
for i in new_text:
    text += i
print(text)
