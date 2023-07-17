import numpy as np
import cv2
from matplotlib import pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Pilulas.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
img = cv2.imread ( CaminhoImagem + NomeImagem, cv2.IMREAD_COLOR)
hh, ww = img.shape[:2]

# 
########################################################################
# Definindo Limites Superiores e Inferiores
########################################################################
#
lower = np.array([200, 200, 200])
upper = np.array([255, 255, 255])

# 
########################################################################
# Criando a Máscara
########################################################################
#
thresh = cv2.inRange(img, lower, upper)

# 
########################################################################
# Aplicando a Morfologia
########################################################################
#
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 
########################################################################
# Invertendo a Morfologia da Imagem
########################################################################
#
mask = 255 - morph

# 
########################################################################
# Aplicando a Máscara na Imagem
########################################################################
#
result = cv2.bitwise_and(img, img, mask=mask)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
morph = cv2.cvtColor(morph, cv2.COLOR_BGR2RGB)
mask  = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,5,1)
plt.imshow(img )
plt.title("Original")

Grafico.add_subplot(1,5,2)
plt.imshow(thresh )
plt.title("Imagem Limite")

Grafico.add_subplot(1,5,3)
plt.imshow(morph )
plt.title("Imagem Mofológica")

Grafico.add_subplot(1,5,4)
plt.imshow(mask )
plt.title("Imagem Máscara")

Grafico.add_subplot(1,5,5)
plt.imshow(result )
plt.title("Imagem Resultado")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
