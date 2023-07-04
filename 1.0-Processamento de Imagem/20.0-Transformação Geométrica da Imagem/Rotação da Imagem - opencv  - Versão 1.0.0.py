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
NomeImagem  = "gato.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
nLinhas, nColunas, nCanais = Imagem.shape

# 
########################################################################
# Rotacionando a Imagem
########################################################################
#
Matriz = cv.getRotationMatrix2D(((nColunas-1)/2.0,(nLinhas-1)/2.0),45,1)
ImagemRotacionada = cv.warpAffine(Imagem,Matriz,(nColunas,nLinhas))

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", Imagem )
cv.setWindowTitle("JanelaBase", "Imagem Original" )

cv.imshow ( "JanelaRotacionada", ImagemRotacionada )
cv.setWindowTitle("JanelaRotacionada", "Rotação de Imagem" )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
