import cv2
import numpy as np
import matplotlib.pyplot as plt

from Projeto import *

def verifica(img):
    
    imagem_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Defina o intervalo de cores vermelhas no espaço de cores HSV
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # Crie uma máscara para a cor vermelha
    mask = cv2.inRange(imagem_hsv, lower_red, upper_red)

    percentage_red = np.sum(mask) / (img.shape[0] * img.shape[1])

    if percentage_red < 0.1:

        return 'Não vermelho'

    else:
        return "Vermelho"



print(verifica(boa1))