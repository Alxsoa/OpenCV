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
NomeJanela = "Imagem Base"
NomeImagem  = "audi.jpg"
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
# Reduzindo o Tamanho
########################################################################
#
EscalaPercentual = 70
LarguraAlterada = int(Imagem.shape[1] * EscalaPercentual / 100)
AlturaAlterada  = int(Imagem.shape[0] * EscalaPercentual / 100)
NovoTamanho = (LarguraAlterada, AlturaAlterada)
NovoTamanho = cv.resize(Imagem, NovoTamanho, interpolation = cv.INTER_AREA)

# 
########################################################################
# Desenhando o Triangulo
########################################################################
#
ImagemAlturaCentral  = int(NovoTamanho.shape[0]/2)
ImagemLarguraCentral = int(NovoTamanho.shape[1]/2)
Lado = 200

LarguraLinha = 9
CorLinha = (0, 0, 255 )
Pontos = [(ImagemLarguraCentral-Lado, ImagemAlturaCentral), (ImagemLarguraCentral+Lado, ImagemAlturaCentral), (ImagemLarguraCentral, ImagemAlturaCentral-Lado)]
NovaImagem =  cv.polylines(NovoTamanho, np.array([Pontos]), True, CorLinha, 5)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", NovaImagem)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

