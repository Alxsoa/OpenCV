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
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
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
LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoInicial = (0,175)
PontoFinal = (344, 516 )
NovaImagem = cv.rectangle(ImagemReduzida, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

# 
########################################################################
# Recortando a Imagem
########################################################################
#
RecorteImagem = ImagemReduzida[175:516, 0:344]

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemOriginal = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
NovaImagem = cv.cvtColor(ImagemReduzida, cv.COLOR_BGR2RGB)
RecorteImagem = cv.cvtColor(RecorteImagem, cv.COLOR_BGR2RGB)

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
plt.imshow(RecorteImagem )
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
