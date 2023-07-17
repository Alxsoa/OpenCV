# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import imutils

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Rotação de Imagens"
NomeImagem  = "gato.jpg"
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
# Rotacionando a Imagem
########################################################################
#
ImagemRotacionada = imutils.rotate(Imagem, angle=45)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", Imagem)
cv.imshow ( "JanelaBase" , ImagemRotacionada )
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
