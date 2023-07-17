# Referencia
# https://github.com/spmallick/learnopencv/blob/master/Image-Inpainting/inpaint.py

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np

def show():
    cv.imshow(NomeJanela, imgFoto)
    cv.imshow(NomeJanela + ": mask", imgMascara)

def ExecutaTracado(Evento,x,y,flags,param):
    global ix,iy,Desenho,ModoExecucao, imgMascara

    if Evento == cv.EVENT_LBUTTONDOWN:       
       Desenho = True
       ix,iy = x,y

    elif Evento == cv.EVENT_MOUSEMOVE:
         if Desenho == True:
            if ModoExecucao == True:
                cv.line (imgFoto,(ix,iy),(x,y),(0, 0, 255), 2)
                cv.line (imgMascara,(ix,iy),(x,y),(0, 0, 255), 2)
                ix,iy = x,y
                cv.imshow(NomeJanela, imgFoto)
                cv.imshow(NomeJanela + ": mask", imgMascara)

    elif Evento == cv.EVENT_LBUTTONUP:
         Desenho = False
         if ModoExecucao == True:
            cv.line (imgFoto,(ix,iy),(x,y),(0, 0, 255), 2)
            cv.line (imgMascara,(ix,iy),(x,y),(0, 0, 255), 2)
            ix,iy = x,y
            cv.imshow(NomeJanela, imgFoto)
            cv.imshow(NomeJanela + ": mask", imgMascara)

    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela  = "Imagem Base"
ImagemBase  = "FotoAntiga.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 
Desenho = False
ModoExecucao  = True 
ix,iy = -1,-1
global  imgMascara

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgFoto = cv.imread ( CaminhoImagem + ImagemBase, cv.IMREAD_COLOR)
Altura, Largura, Cor = imgFoto.shape

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgFoto is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", ImagemBase)
    exit ()

# 
########################################################################
# Criando a Máscara
########################################################################
#
imgMascara = np.full([Altura, Largura,3], (0, 0, 0), dtype=np.uint8)

# 
########################################################################
# Janelamento e Instancia de Função
########################################################################
#
cv.imshow(NomeJanela, imgFoto)
cv.imshow(NomeJanela + ": mask", imgMascara)
cv.setMouseCallback(NomeJanela, ExecutaTracado)

# 
########################################################################
# Loop de Execução
########################################################################
#
while(True):
    cv.imshow(NomeJanela, imgFoto)
    cv.imshow(NomeJanela + ": mask", imgMascara)

    k = cv.waitKey(1) & 0xFF
    if k == ord('e'):
        ModoExecucao = not ModoExecucao
        imgMascara = cv.cvtColor(imgMascara,cv.COLOR_RGB2GRAY)
        imgFoto = cv.cvtColor(imgFoto,cv.COLOR_RGB2GRAY)
        res = cv.inpaint(imgFoto, imgMascara, 3, cv.INPAINT_TELEA)
        cv.imshow('Resultado Usando Metodo FMM', res)

    elif k == 27:
        break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
e