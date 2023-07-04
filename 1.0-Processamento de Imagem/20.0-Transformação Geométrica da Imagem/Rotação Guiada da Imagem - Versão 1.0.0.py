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
NomeJanela = "Imagem Base"
NomeImagem  = "Moda.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 
LarguraLinha = 1
CorLinha = (0, 0, 255 )
Raio = 4

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
nLinhas, nColunas, nCanais = imgReduzida.shape

# 
########################################################################
# Definindo os Pontos Virtuais na Imagem
########################################################################
#
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# 
########################################################################
# Desenhando os Pontos Virtuais na Imagem
########################################################################
#
ImagemVirtual = imgReduzida.copy()
ImagemVirtual = cv.circle(ImagemVirtual, (50, 50), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (200,50), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (50,200), Raio, CorLinha, cv.FILLED)

# 
########################################################################
# Executando a Rotação Guiada
########################################################################
#
Matriz = cv.getAffineTransform(pts1,pts2)
ImagemGuiada = cv.warpAffine(imgReduzida,Matriz,(nColunas,nLinhas))

# 
########################################################################
# Desenhando os Pontos Virtuais na Imagem Guiada
########################################################################
#
ImagemGuiada = cv.circle(ImagemGuiada, (10, 100), Raio, CorLinha, cv.FILLED)
ImagemGuiada = cv.circle(ImagemGuiada, (200,50), Raio, CorLinha, cv.FILLED)
ImagemGuiada = cv.circle(ImagemGuiada, (100,250), Raio, CorLinha, cv.FILLED)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
ImagemVirtual = cv.cvtColor(ImagemVirtual, cv.COLOR_BGR2RGB)
ImagemGuiada = cv.cvtColor(ImagemGuiada, cv.COLOR_BGR2RGB)
# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,3,1)
plt.imshow(imgReduzida )
plt.title("Imagem\nOriginal")

Grafico.add_subplot(1,3,2)
plt.imshow(ImagemVirtual )
plt.title("Imagem\nVirtual")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemGuiada )
plt.title("Imagens\nGuiada")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
