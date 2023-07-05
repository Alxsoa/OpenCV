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
DirBase = "OpenCV/"
CaminhoBase = "/home/asoares/" + DirBase
NomeJanela = "Imagem Reduzida"
NomeImagem  = "audi.jpg"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
cv.imshow ( "Imagem Grande" , Imagem )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#

imgReduzida = cv.resize(Imagem, (450, 300), interpolation = cv.INTER_AREA)
cv.imshow ( "JanelaBase", imgReduzida)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
