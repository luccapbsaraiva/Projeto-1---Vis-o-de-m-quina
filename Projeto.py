import cv2
import numpy as np
import matplotlib.pyplot as plt
from Verifica_Cores import cores
from Verifica_quebrada import quebrada
from verifica_amassada import separa
from verifica_amassada import amassada
from verifica_dimesoes import dimensions
from verifica_dimesoes import position
import pandas as pd

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

validacao1 = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_1.png',1)
validacao1_gray = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_1.png',0)
validacao1_rgb = cv2.cvtColor(validacao1, cv2.COLOR_BGR2RGB)

validacao2 = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_2.png',1)
validacao2_gray = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_2.png',0)
validacao2_rgb = cv2.cvtColor(validacao2, cv2.COLOR_BGR2RGB)

validacao3 = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_3.png',1)
validacao3_gray = cv2.imread('Imagens_TESTE_VALIDACAO/Imagem_VALIDACAO_3.png',0)
validacao3_rgb = cv2.cvtColor(validacao3, cv2.COLOR_BGR2RGB)


pilulas_separdas, imagem_numerada = separa(teste_gray,teste_rgb)

pilulas_amassadas = {}
pilulas_vermelhas={}
pilulas_quebradas={}
pilulas_dimensoes={}

for i in pilulas_separdas:
    verifica_amassada = amassada(pilulas_separdas[i])
    if verifica_amassada == 'ok':
        #print('mantem')
        pilulas_amassadas[i]=pilulas_separdas[i]
        
    else:
        #print('tira')
        pass



for j in pilulas_amassadas:
    verifica_cor = cores(pilulas_amassadas[j])
    if verifica_cor == 'Vermelho':
        #print('mantem')
        pilulas_vermelhas[j]=pilulas_amassadas[j]
    else:
        #print("tira")
        pass


for k in pilulas_vermelhas:
    verifica_quebrada = quebrada(pilulas_vermelhas['img7'],pilulas_vermelhas[k])
    if verifica_quebrada == 'A pilula está integra':
        #print('mantem')
        pilulas_quebradas[k]=pilulas_vermelhas[k]
        #print(k)
    else:
        #print("tira")
        #print(k)
        pass


for v in pilulas_quebradas:
    verifica_dimensoes= dimensions(pilulas_quebradas['img7'],pilulas_quebradas[v])
    print("Pilula: ",v," Dimensão: ",verifica_dimensoes)



posicoes=position(teste_rgb)

for nome, img in pilulas_quebradas.items():
    if nome in posicoes:
        print(f"Pílula: {nome}  Dimensão: {img.shape}  Posição: {posicoes[nome]}")



import csv

# Abra o arquivo CSV em modo de escrita
with open("Resultado_Img_VALIDACAO.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Escreva o cabeçalho
    writer.writerow(["Status", "Pos X", "Pos Y", "W", "H1", "H2"])


    for nome, img in pilulas_separdas.items():
        
        status = "OK"  # Defina um status padrão
        pos_x, pos_y = posicoes[nome]
        w, h1, h2 = verifica_dimensoes 
        
        if nome not in pilulas_amassadas:
            status = "Amassada"
            pos_x, pos_y = 0,0
            w, h1, h2 = 0,0,0      

        elif nome not in pilulas_vermelhas:
            
            status = "Não Vermelho"
            pos_x, pos_y = 0,0
            w, h1, h2 = 0,0,0 

        elif nome not in pilulas_quebradas:
            
            status = "Quebrada"
            pos_x, pos_y = 0,0
            w, h1, h2 = 0,0,0
        
        # Escreva os dados no arquivo CSV
        writer.writerow([nome, status, pos_x, pos_y, w, h1, h2])



fig, axs = plt.subplots(nrows=1, ncols=len(pilulas_quebradas) + 1, figsize=(15, 15))  

axs[0].imshow(imagem_numerada)
axs[0].set_title("Imagem Numerada")

for i, (nome, img) in enumerate(pilulas_quebradas.items()):
    axs[i+1].imshow(img)  
    axs[i+1].set_title(nome)

plt.show()
