# Referencia
# https://pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://ourcodeworld.com/articles/read/991/how-to-calculate-the-structural-similarity-index-ssim-between-two-images-with-python

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as compare_ssim 
import imutils

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeCartaoCompleto = "CartaoCreditoCompleto.jpg"
NomeCartaoSemLogo = "CartaoCreditoSemLogo.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgCartaoCompleto = cv.imread ( CaminhoImagem + NomeCartaoCompleto, cv.IMREAD_COLOR )
if imgCartaoCompleto is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeCartaoCompleto)
   exit ()


imgCartaoSemLogo = cv.imread ( CaminhoImagem + NomeCartaoSemLogo, cv.IMREAD_COLOR )
if imgCartaoSemLogo is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeCartaoSemLogo )
   exit ()

# 
########################################################################
# Transformando para Tons de Cinza
########################################################################
#
imgCartaoCompletoCinza = cv.cvtColor(imgCartaoCompleto, cv.COLOR_BGR2GRAY)
imgCartaoSemLogoCinza = cv.cvtColor(imgCartaoSemLogo, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Calcula o SSI com Retorno da Imagem
########################################################################
#
(Escore, imgDiferenca) = compare_ssim(imgCartaoCompletoCinza, imgCartaoSemLogoCinza, full=True)
imgDiferenca = (imgDiferenca * 255).astype("uint8")
print("SSIM: {}".format(Escore))

# 
########################################################################
# Limita a Diferença da Imagem e Seguidamente Encontra as 
# Regiões de Diferença das duas Imagens 
########################################################################
#
Limiar = cv.threshold(imgDiferenca, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
Contorno = cv.findContours(Limiar.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
Contorno = imutils.grab_contours(Contorno)

# 
########################################################################
# Calcula a Caixa Delimitadora do Contorno e, em Seguida, Desenha a 
# Caixa Delimitadora em Ambas as Imagens 
########################################################################
#
for lstContorno in Contorno:
	(xPts, yPts, Largura, Altura) = cv.boundingRect(lstContorno)
	cv.rectangle(imgCartaoCompleto, (xPts, yPts), (xPts + Largura, yPts + Altura), (0, 0, 255), 2)
	cv.rectangle(imgCartaoSemLogo, (xPts, yPts), (xPts + Largura, yPts+ Altura), (0, 0, 255), 2)
# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgCartaoCompleto = cv.cvtColor(imgCartaoCompleto, cv.COLOR_BGR2RGB)
imgCartaoSemLogo = cv.cvtColor(imgCartaoSemLogo, cv.COLOR_BGR2RGB)
imgDiferenca = cv.cvtColor(imgDiferenca, cv.COLOR_BGR2RGB)
imgLimiar = cv.cvtColor(Limiar, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,14))

Grafico.add_subplot(2,2,1)
plt.imshow(imgCartaoCompleto )
plt.title("Cartão Original")

Grafico.add_subplot(2,2,2)
plt.imshow(imgCartaoSemLogo )
plt.title( "Cartão Incompleto" )

Grafico.add_subplot(2,2,3)
plt.imshow(imgDiferenca )
plt.title("Diferença")

Grafico.add_subplot(2,2,4)
plt.imshow(imgLimiar )
plt.title("Limiar")

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.3 )

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################	
