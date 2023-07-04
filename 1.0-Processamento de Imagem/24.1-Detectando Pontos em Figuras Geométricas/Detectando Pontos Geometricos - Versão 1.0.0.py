# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import cv2
from matplotlib import pyplot as plt
  
# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "FormasGeometricas.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Convertendo para Cinza a Imagem
########################################################################
#
imgBase  = cv2.imread(CaminhoImagem+NomeImagem)
imgCinza = cv2.cvtColor(imgBase, cv2.COLOR_BGR2GRAY)

# 
########################################################################
# Detectando os Cornes 
########################################################################
#  
Corners = cv2.goodFeaturesToTrack(imgCinza, 29, 0.01, 10)
Corners = np.intp(Corners)
  
# 
########################################################################
# Desenhando o Indicativo do Corner
########################################################################
#
for iAux in Corners:
    xPosicao, yPosicao = iAux.ravel()
    cv2.circle(imgBase, (xPosicao, yPosicao), 5, 255, -1)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv2.cvtColor(imgBase, cv2.COLOR_BGR2RGB)  

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.imshow(imgBase)
plt.show()
