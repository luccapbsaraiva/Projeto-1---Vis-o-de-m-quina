import cv2
import numpy as np
import matplotlib.pyplot as plt
from Verifica_Cores import cores
from Verifica_quebrada import quebrada
from verifica_amassada import separa
from verifica_amassada import amassada
from verifica_dimesoes import dimensions
from verifica_dimesoes import position

boa1 = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_01.png', 1)
boa2 = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_02.png', 1)
boa3 = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_03.png', 1)
boa4 = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_04.png', 1)
boa5 = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_05.png', 1)


amassada1 = cv2.imread('Imagens_DESENVOLVIMENTO/amassada1.png', 1) 
amassada2 = cv2.imread('Imagens_DESENVOLVIMENTO/amassada2.png', 1)
amassada3 = cv2.imread('Imagens_DESENVOLVIMENTO/amassada3.png', 1)

color1 = cv2.imread('Imagens_DESENVOLVIMENTO/color1.png',1)
color3  = cv2.imread('Imagens_DESENVOLVIMENTO/color3.png',1)

quebrada1 = cv2.imread('Imagens_DESENVOLVIMENTO/quebrada_01.png',1)
quebrada2 = cv2.imread('Imagens_DESENVOLVIMENTO/quebrada_02.png',1)
quebrada3 = cv2.imread('Imagens_DESENVOLVIMENTO/quebrada_03.png',1)

riscada1 = cv2.imread('Imagens_DESENVOLVIMENTO/riscada1.png',1)
riscada2 = cv2.imread('Imagens_DESENVOLVIMENTO/riscada2.png',1)

teste = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_TESTE_0.png',1)
teste_gray = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_TESTE_0.png',0)
teste_rgb = cv2.cvtColor(teste, cv2.COLOR_BGR2RGB)

contorno=separa(teste_gray,teste_rgb)


x,y,z=contorno['img1'].shape

h,w,c=boa1.shape
print("Normal ",h,w)
print("Corte ",x,y)

plt.imshow(contorno['img9'])
plt.show()


#print(quebrada(contorno['img1'],contorno['img3']))

amassada(contorno['img9'])


boa1_rgb = cv2.cvtColor(boa1, cv2.COLOR_BGR2RGB)
print(dimensions(contorno['img3'],boa1_rgb))


teste2_rgb = cv2.cvtColor(cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_TESTE_0.png', 1), cv2.COLOR_BGR2RGB)

print(position(teste2_rgb)['img{0}'.format(1)])




