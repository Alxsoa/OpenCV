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
# Desenhando a Elipse
########################################################################
#
ImagemAltura = int(NovoTamanho.shape[0]/2)
ImagemLargura = int(NovoTamanho.shape[1]/2)

LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoCentral = (ImagemLargura,ImagemAltura )
axes = 100, 60
angle = 0

NovoTamanho = cv.ellipse(NovoTamanho, PontoCentral, axes, angle, 0, 360, CorLinha, LarguraLinha)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", NovoTamanho)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
