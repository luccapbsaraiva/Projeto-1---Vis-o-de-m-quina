import cv2
import numpy as np
import matplotlib.pyplot as plt


def quebrada(img):

    img_molde = cv2.imread('Imagens_DESENVOLVIMENTO/_boa_01.png', 1)
    img_boa=cv2.cvtColor(img_molde, cv2.COLOR_BGR2RGB)

    img_ruim=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #########################################
    # Para a parte preta da pilula

    pilula_boa = cv2.cvtColor(img_molde, cv2.COLOR_BGR2GRAY)
    pilula_amassada = cv2.cvtColor(img_ruim, cv2.COLOR_BGR2GRAY)
    threshold_preto = np.where(pilula_boa > 50, 255,0).astype('uint8')

    nova_preto=cv2.cvtColor(threshold_preto, cv2.COLOR_GRAY2RGB)

    bitwiseOr_preto = cv2.bitwise_or(nova_preto,img_ruim)


    imagem_hsv = cv2.cvtColor(bitwiseOr_preto, cv2.COLOR_RGB2HSV)


    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # Crie a máscara
    mask = cv2.inRange(imagem_hsv, lower_red, upper_red)

    # Calcule a porcentagem novamente
    percentage_red = np.sum(mask) / (bitwiseOr_preto.shape[0] * bitwiseOr_preto.shape[1])

    #######################################
    # Para a parte vermelha da pilula
    hsv_vermelho = cv2.cvtColor(img_boa, cv2.COLOR_RGB2HSV)

    # Crie uma máscara para o cinza
    mask = cv2.inRange(hsv_vermelho, lower_red, upper_red)

    # Aplique a máscara à imagem
    separa_vermelho = cv2.bitwise_and(img_boa, img_boa, mask=mask)

    pilula_vermelha = cv2.cvtColor(separa_vermelho, cv2.COLOR_RGB2GRAY)
    threshold_vermelho = np.where(pilula_vermelha > 50, 255,0).astype('uint8')

    nova_vermelho=cv2.cvtColor(threshold_vermelho, cv2.COLOR_GRAY2RGB)
    bitwiseOr_vermelho = cv2.bitwise_and(nova_vermelho,img_ruim)
    
    plt.imshow(bitwiseOr_vermelho)
    plt.show()


    if np.any(bitwiseOr_vermelho == 255) or percentage_red > 0.9:
        return "A pilula está quebrada"
    else:
        return "A pilula está integra" 

    












