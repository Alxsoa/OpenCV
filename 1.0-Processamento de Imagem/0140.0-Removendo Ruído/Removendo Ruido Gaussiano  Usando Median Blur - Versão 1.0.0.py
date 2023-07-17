# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
ImagemOriginal  = 'Caravela.jpg'
ImagemRuido  = 'CaravelaRuidoGausiano.jpg'
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemOriginal= cv.imread ( CaminhoImagem + ImagemOriginal, cv.IMREAD_COLOR)
ImagemRuido = cv.imread ( CaminhoImagem + ImagemRuido, cv.IMREAD_COLOR)

# 
########################################################################
# Removendo o Ruído  
########################################################################
#
ImagemSemRuido = cv.medianBlur(ImagemRuido,3)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgCaravela = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
imgRuido = cv.cvtColor(ImagemRuido, cv.COLOR_BGR2RGB)
imgSemRuido = cv.cvtColor(ImagemSemRuido, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,3,1)
plt.imshow(imgCaravela )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(imgRuido )
plt.title("Imagem Ruído")

Grafico.add_subplot(1,3,3)
plt.imshow(imgSemRuido )
plt.title("Imagem\nsem Ruído")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

