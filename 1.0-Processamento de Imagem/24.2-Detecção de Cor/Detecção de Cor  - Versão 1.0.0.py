
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np 

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela  = "Imagem Base"
NomeImagem  = "PastaAzul.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Convertendo os Frames BGR para HSV
########################################################################
#
hsvCor = cv.cvtColor(Imagem, cv.COLOR_BGR2HSV)
baixoAzul = np.array([110,50,50])
altoAzul  = np.array([130,255,255])
  
# 
########################################################################
# Investigando as Cores Baseadas nos Limites Definidos (Mask)
########################################################################
#
Mascara = cv.inRange(hsvCor, baixoAzul, altoAzul)
  
# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgResultado = cv.bitwise_and (Imagem, Imagem, mask = Mascara)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", Imagem)
cv.setWindowTitle("JanelaBase", "Imagem Original" )

cv.imshow ( "MascaraJanela", Imagem)
cv.setWindowTitle("MascaraJanela", "Máscara da Imagem" )

cv.imshow ( "JanelaResultado", Imagem)
cv.setWindowTitle("JanelaResultado", "Imagem Resultado" )

cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
