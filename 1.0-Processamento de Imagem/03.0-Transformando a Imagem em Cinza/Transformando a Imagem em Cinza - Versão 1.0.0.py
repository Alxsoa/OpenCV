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
ImagemColorida = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Transformando para Tons de Cinza
########################################################################
#
ImagemCinza = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Apresentando a Imagem Colorida
########################################################################
#
cv.imshow ( "JanelaBase", ImagemCinza)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

# 
########################################################################
# Apresentando a Imagem Cinza
########################################################################
#
cv.imshow ( NomeJanela , ImagemCinza )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
