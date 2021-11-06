import cv2 as cv
import numpy as np


img = cv2.imread("001.jpeg",0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

img_write = Image.fromarray(cl_img)
img_write.save("teste.jpg")