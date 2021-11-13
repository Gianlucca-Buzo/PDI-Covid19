import numpy as np
from skimage import io, img_as_float
import imquality.brisque as brisque

def brisque(name):
    print("Cheguei aqui 1")
    img = img_as_float(io.imread('imagens/'+name+'/Original.png',as_gray=True))
    img_clahe = img_as_float(io.imread('imagens/'+name+'/CLAHE.png',as_gray=True))
    img_he = img_as_float(io.imread('imagens/'+name+'/HistogramEqualization.png',as_gray=True))
    img_beasf = img_as_float(io.imread('imagens/'+name+'/BEASF.png',as_gray=True))
    img_gamma = img_as_float(io.imread('imagens/'+name+'/Gamma.png',as_gray=True))
    print("Cheguei aqui 1")
    score_original = brisque.score(img)
    score_clahe = brisque.score(img_clahe)
    score_he = brisque.score(img_he)
    score_beasf = brisque.score(img_beasf)
    score_gamma = brisque.score(img_gamma)
    print("Cheguei aqui 2")
    print('Score Lower is better')
    print("Brisque score of original image"+ name+" is =",score_original)
    print("Brisque score of BEASF image"+ name+" is =",score_beasf)
    print("Brisque score of CLAHE image"+ name+" is =",score_clahe)
    print("Brisque score of HE image is"+ name+" =",score_he)
    print("Brisque score of GAMMA image"+ name+" is =",score_gamma)

if __name__ == '__main__':
    brisque('004')