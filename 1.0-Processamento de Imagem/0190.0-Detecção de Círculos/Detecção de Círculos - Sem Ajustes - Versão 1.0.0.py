# Referencia
# https://medium.com/turing-talks/houghcircles-detec%C3%A7%C3%A3o-de-c%C3%ADrculos-em-imagens-com-opencv-e-python-2d229ad9d43b

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Bicicleta.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem ) 

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgBase = cv.resize(imgBase,(0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Buscando a Existencia de Círculos
########################################################################
#
Circulos = cv.HoughCircles (
                            imgCinza,
                            cv.HOUGH_GRADIENT,
                            dp = 0.9,
                            minDist = 300,
                            param1 = 200,
                            param2 = 40,
                            minRadius = 50, 
                            maxRadius = 400)
#print(Circulos)

# 
########################################################################
# Mostrando o Círculo
########################################################################
#
circles = np.uint16(np.around(Circulos))
imgCirculos = imgBase.copy()

for i in circles[0,:]:
#   Desenhando o círculo externo (Verde)
    cv.circle(imgCirculos,(i[0],i[1]),i[2],(0, 255, 128) ,5)

#   Desenhando o círculo interno (Vermelho)
    cv.circle(imgCirculos,(i[0],i[1]),2,(0,0,255),5)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", imgCirculos )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
