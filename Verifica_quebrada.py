import cv2
import numpy as np
import matplotlib.pyplot as plt


from Projeto import *

#def verifica_quebrada(img):

img = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_01.png', 1)
img_ruim=cv2.cvtColor(quebrada2, cv2.COLOR_BGR2RGB)

pilula_boa = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
pilula_amassada = cv2.cvtColor(img_ruim, cv2.COLOR_BGR2GRAY)
threshold_boa = np.where(pilula_boa > 50, 255,0).astype('uint8')

nova=cv2.cvtColor(threshold_boa, cv2.COLOR_GRAY2RGB)

bitwiseOr = cv2.bitwise_or(nova,img_ruim)


imagem_hsv = cv2.cvtColor(bitwiseOr, cv2.COLOR_RGB2HSV)


lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])


# Crie a máscara
mask = cv2.inRange(imagem_hsv, lower_red, upper_red)

# Calcule a porcentagem novamente
percentage_red = np.sum(mask) / (bitwiseOr.shape[0] * bitwiseOr.shape[1])

print(percentage_red)

#plt.imshow(bitwiseOr)

#plt.show()


















