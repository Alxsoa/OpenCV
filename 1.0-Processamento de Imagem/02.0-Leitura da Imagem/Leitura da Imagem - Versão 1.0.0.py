# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
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
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", Imagem)
cv.setWindowTitle("JanelaBase", NomeJanela )

cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
