# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "Baloes.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 
EscalaPercentual = 0.5

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem )

# 
########################################################################
# Calculando o Histograma
########################################################################
#
HistogramaAzul  = cv.calcHist([ImagemBase], [0],None,[256],[0,256])
HistogramaVerde = cv.calcHist([ImagemBase], [1],None,[256],[0,256])
HistogramaVermelho = cv.calcHist([ImagemBase], [2],None,[256],[0,256])

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,2,1)
plt.plot(HistogramaAzul,color = "b")
plt.plot(HistogramaVerde,color = "g")
plt.plot(HistogramaVermelho,color = "r")
plt.xlim([0,256])
plt.title("Histograma")

ImagemBase = cv.cvtColor(ImagemBase, cv.COLOR_BGR2RGB)
Grafico.add_subplot(1,2,2)
plt.imshow(ImagemBase )
plt.axis("off")
plt.title("Imagem\nOriginal")
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
