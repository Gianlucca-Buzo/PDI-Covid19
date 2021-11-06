from BEASF import BEASF
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    print("Iniciando BEASF")
    image = Image.open('001.jpeg')
    print(type(image))
    print(image)
    imageAsArray = np.asarray(image)
    print(imageAsArray)
    a = BEASF(image=imageAsArray,gamma=1.5)
    img = Image.fromarray(a)
    img.save('imagemBEASF.jpeg')