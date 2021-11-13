import numpy as np
# from skimage import io, img_as_float
import imquality.brisque as brisque
import cv2
import numpy as np
from matplotlib import pyplot as plt
from BEASF import BEASF
import os
from gamma import gammaCorrection
from brisque import brisque
#gamma corretion function


#load image
if __name__ == '__main__':
    images = ['004.jpeg','011.jpeg','024.jpg','029.jpg','042.png']
    for i in range(0,len(images)):
        image = images[i]
        nome = image.split(".")[0]
        img = cv2.imread('imagens/'+image ,0)
        hist_eq = cv2.equalizeHist(img) #perform histogram equalization
        complement = 255 - img # perform image complement
        gammaImg = gammaCorrection(img,1.5) # perform a y = 2.2 gamma correction
        beasf_img = BEASF(image=img,gamma=1.5) #perform beasf enhancement
        clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
        clahe_img = clahe.apply(img)
        try:
            os.mkdir('imagens/'+nome)
            cv2.imwrite('imagens/'+nome+ '/HistogramEqualization.png',hist_eq)
            cv2.imwrite('imagens/'+nome+ '/Complement.png',complement)
            cv2.imwrite('imagens/'+nome+ '/Gamma.png',gammaImg)
            cv2.imwrite('imagens/'+nome+ '/BEASF.png',beasf_img)
            cv2.imwrite('imagens/'+nome+ '/CLAHE.png',clahe_img)
            cv2.imwrite('imagens/'+nome+ '/Original.png', img)
            # brisque(nome)
        except:
            print("Erro na imagem "+ image)
