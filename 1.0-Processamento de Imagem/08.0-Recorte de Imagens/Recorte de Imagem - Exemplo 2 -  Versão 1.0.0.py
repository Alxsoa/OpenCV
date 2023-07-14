# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# 
########################################################################
# Funções de Apoio
########################################################################
#
def AproximaImagem ( imgTmpImagem, iFator ):
    return (cv.resize(imgTmpImagem, None, fx=iFator, fy=iFator))

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Mesa.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()
# 
########################################################################
# Reduzindo o Tamanho
########################################################################
#
EscalaPercentual = 10
LarguraAlterada = int(Imagem.shape[1] * EscalaPercentual / 100)
AlturaAlterada  = int(Imagem.shape[0] * EscalaPercentual / 100)
NovoTamanho = (LarguraAlterada, AlturaAlterada)
ImagemReduzida = cv.resize(Imagem, NovoTamanho, interpolation = cv.INTER_AREA)
ImagemOriginal = ImagemReduzida.copy ()

# 
########################################################################
# Desenhando o Retangulo
########################################################################
#
LarguraLinha = 3
CorLinha = (0, 0, 255 )
PontoInicial = (160, 230)
PontoFinal = (257, 332)
NovaImagem = cv.rectangle(ImagemReduzida, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

# 
########################################################################
# Recortando a Imagem
########################################################################
#
RecorteImagem = NovaImagem[230:332, 160:257]

# 
########################################################################
# Aumentando a Imagem
########################################################################
#
imgAumentada = AproximaImagem (RecorteImagem, 3)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemOriginal = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
NovaImagem = cv.cvtColor(ImagemReduzida, cv.COLOR_BGR2RGB)
imgAumentada = cv.cvtColor(imgAumentada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure(figsize=(14,8))

Grafico.add_subplot(1,3,1)
plt.imshow( ImagemOriginal )
plt.title("Imagem\nOriginal")

Grafico.add_subplot(1,3,2)
plt.imshow(NovaImagem )
plt.title("Recorte\nProjetado")

Grafico.add_subplot(1,3,3)
plt.imshow(imgAumentada )
plt.title("Imagem\nResultado")

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.1 )

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
