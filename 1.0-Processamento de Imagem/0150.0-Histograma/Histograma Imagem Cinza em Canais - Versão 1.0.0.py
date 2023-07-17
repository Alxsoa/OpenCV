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
NomeImagem  = "Farol.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 
EscalaPercentual = 0.5

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem, 0 ) 

# 
########################################################################
# Gerando o Histograma
########################################################################
#
ImagemHistograma = cv.calcHist([ImagemBase], [0], None, [256], [0, 256])
ImagemBase = cv.cvtColor(ImagemBase, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,2,1)
plt.plot(ImagemHistograma)
plt.title("Histograma")

Grafico.add_subplot(1,2,2)
plt.imshow(ImagemBase )
plt.axis("off")
plt.title("Imagem\nOriginal")
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
