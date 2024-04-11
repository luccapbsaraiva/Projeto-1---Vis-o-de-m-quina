import cv2
import numpy as np
import matplotlib.pyplot as plt
from Projeto import *

boa_rgb = cv2.cvtColor(boa1, cv2.COLOR_BGR2RGB)
boa1_gray = cv2.cvtColor(boa1, cv2.COLOR_BGR2GRAY)
boa2_gray = cv2.cvtColor(boa2, cv2.COLOR_BGR2GRAY)
boa3_gray = cv2.cvtColor(boa3, cv2.COLOR_BGR2GRAY)
boa4_gray = cv2.cvtColor(boa4, cv2.COLOR_BGR2GRAY)
boa5_gray = cv2.cvtColor(boa5, cv2.COLOR_BGR2GRAY)

amassada1_gray = cv2.cvtColor(amassada1, cv2.COLOR_BGR2GRAY)
amassada2_gray = cv2.cvtColor(amassada2, cv2.COLOR_BGR2GRAY)
amassada3_gray = cv2.cvtColor(amassada3, cv2.COLOR_BGR2GRAY)

teste = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_TESTE_0.png',1)
teste_gray = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_TESTE_0.png',0)
teste_rgb = cv2.cvtColor(teste, cv2.COLOR_BGR2RGB)

lista_boas = [boa1_gray, boa2_gray, boa3_gray, boa4_gray, boa5_gray]

lista_amassadas = [amassada1_gray, amassada2_gray, amassada3_gray]

def verifica_amassada(img_gray, img_rgb):
    ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
    thresh = cv2.bitwise_not(thresh)

    contours, hierarchy = cv2.findContours(thresh,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    min = 120
    filtra_contours = [contour for contour in contours if len(contour)> min]
    contornos = cv2.drawContours(img_rgb, filtra_contours,-1, (0,0,255), 2)
    i = 0
    area_real = []
    pilula_index = []
    for cnt in filtra_contours:
        M = cv2.moments(cnt)
        cX = int(M['m10']/M['m00'])
        cY = int(M["m01"]/M['m00'])
        cv2.putText(img_rgb, f"{i+1}", (cX-300,cY-100), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,0,0), 8)
        area = cv2.contourArea(cnt)
        if area>50000.0 and area<54000.0:
            area_real.append(area)
            pilula_index.append(i+1)
        i +=1
    print(area_real)
    print('---------------------')
    print(pilula_index)
    return contornos


'''for boa in lista_boas:
    verifica_amassada(boa)
print('---------------------------')
for amassada in lista_amassadas:
    verifica_amassada(amassada)

'''
saida = verifica_amassada(teste_gray, teste_rgb)

fig = plt.figure(figsize=(10,10))
fig.add_subplot(1,2,1)
plt.imshow(teste_gray, cmap='gray')
fig.add_subplot(1,2,2)
plt.imshow(saida, cmap="gray")
plt.show()
