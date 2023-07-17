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
# Desenhando o Retangulo
########################################################################
#
ImagemAltura = NovoTamanho.shape[0]
ImagemLargura = NovoTamanho.shape[1]

LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoInicial = (0,0)
PontoFinal = (ImagemLargura,ImagemAltura )
NovaImagem = cv.rectangle(NovoTamanho, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

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
