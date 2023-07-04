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
NomeJanela = "Imagem Reduzida"
NomeImagem  = "audi.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
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

imgReduzida = cv.resize(Imagem, (0,0), fx=0.3, fy=0.5, interpolation = cv.INTER_AREA)
cv.imshow ( "JanelaBase", imgReduzida)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
