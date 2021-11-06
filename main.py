from BEASF import BEASF
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2

if __name__ == '__main__':
    print("Iniciando BEASF")
    
    image = Image.open('001.jpeg')
    imageAsArray = np.asarray(image)
    a = BEASF(image=imageAsArray,gamma=1.5)
    img = Image.fromarray(a)
    img.save('imagemBEASF.jpeg')
