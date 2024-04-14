import cv2
import numpy as np
import matplotlib.pyplot as plt


def dimensions(img, img_molde):
    #PRECISA DE UMA IMAGEM MOLDE CORRETA DA BASE DE DESENVOLVIMENTO PRA RODAR
    img_boa = img_molde
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
    thresh = cv2.bitwise_not(thresh)

    contours, hierarchy = cv2.findContours(thresh,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    min_val = 120
    filtra_contours = [contour for contour in contours if len(contour)> min_val]
    for cnt in filtra_contours:
        x, y, w, h1 = cv2.boundingRect(cnt)

#############################
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    hsv_vermelho = cv2.cvtColor(img_boa, cv2.COLOR_RGB2HSV)

    # Crie uma máscara para o cinza
    mask = cv2.inRange(hsv_vermelho, lower_red, upper_red)

    # Aplique a máscara à imagem
    separa_vermelho = cv2.bitwise_and(img_boa, img_boa, mask=mask)

    pilula_vermelha = cv2.cvtColor(separa_vermelho, cv2.COLOR_RGB2GRAY)
    threshold_vermelho = np.where(pilula_vermelha > 50, 255,0).astype('uint8')


    contours_cor, hierarchy_cor = cv2.findContours(threshold_vermelho,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtra_contours_cor = [contour for contour in contours_cor if len(contour)> min_val]
    for cnt in filtra_contours_cor:
        x_cor, y_cor, w_cor, h2 = cv2.boundingRect(cnt)

##################################
    # Retorna as dimensões nessa ordem
    return w, h1, h2
    