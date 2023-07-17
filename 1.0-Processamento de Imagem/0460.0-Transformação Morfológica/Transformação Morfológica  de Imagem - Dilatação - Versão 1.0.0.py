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
NomeJanela  = "Imagem Base"
NomeImagem  = "Casa.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem )

# 
########################################################################
# Calculando a Erosão
########################################################################
#
Kernel = np.ones((3,3), np.uint8)
imgErosao = cv.dilate(imgBase, Kernel, iterations=3)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
imgErosao = cv.cvtColor(imgErosao, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,2,1)
plt.imshow(imgBase )
plt.title("Original")

Grafico.add_subplot(1,2,2)
plt.imshow ( imgErosao )
plt.title("Resultado\nDilatação")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
