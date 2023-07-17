# Referencia
# https://theailearner.com/tag/cv2-warpperspective/

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
NomeImagem  = "QuadroPerspectiva.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
#imgReduzida = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

cv.imshow ( "JanelaBase", imgBase )
cv.waitKey(0)
cv.destroyAllWindows()

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgEsquerda = cv.cvtColor (imgEsquerda, cv.COLOR_BGR2RGB)
imgDireita  = cv.cvtColor (imgDireita,  cv.COLOR_BGR2RGB)
imgSuperior = cv.cvtColor (imgSuperior, cv.COLOR_BGR2RGB)
imgInferior = cv.cvtColor (imgInferior, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
#Grafico = plt.figure(figsize=(11,8))

#Grafico.add_subplot(2,2,1)
#plt.imshow(imgEsquerda )
#plt.title("Translação Esquerda", fontsize=11, weight='bold' )

#Grafico.add_subplot(2,2,2)
#plt.imshow(imgDireita )
#plt.title("Translação Direita", fontsize=11, weight='bold' )

#Grafico.add_subplot(2,2,3)
#plt.imshow(imgSuperior )
#plt.title("Translação Superior", fontsize=11, weight='bold' )

#Grafico.add_subplot(2,2,4)
#plt.imshow(imgInferior )
#plt.title("Translação Inferior", fontsize=11, weight='bold' )

#plt.subplots_adjust ( left   = 0.1,
#                      bottom = 0.1,
#                      right  = 0.9,
#                      top    = 0.9,
#                      wspace = 0.2,
#                      hspace = 0.2 )
#plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
