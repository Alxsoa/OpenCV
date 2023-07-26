# Referencia
# https://pyimagesearch.com/2021/01/23/splitting-and-merging-channels-with-opencv/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/"  

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemColorida = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemColorida is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Reduzindo a Imagem
########################################################################
#
ImagemColorida = cv.resize ( ImagemColorida, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Azul, Verde, Vermelho = cv.split(ImagemColorida)
zeros = np.zeros(ImagemColorida.shape[:2], dtype="uint8")
Vermelho = cv.merge([zeros, zeros, Vermelho])
Verde = cv.merge([zeros, Verde, zeros])
Azul = cv.merge([Azul, zeros, zeros])

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
#
cv.imwrite( CaminhoImagem+"GirassolAzul.png", Azul)
cv.imwrite( CaminhoImagem+"GirassolVerde.png", Verde)
cv.imwrite( CaminhoImagem+"GirassolVermelho.png", Vermelho)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgAzul = cv.cvtColor(Azul, cv.COLOR_BGR2RGB)
imgVerde = cv.cvtColor(Verde, cv.COLOR_BGR2RGB)
imgVermelho = cv.cvtColor(Vermelho, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,8))

Grafico.add_subplot(1,4,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(1,4,2)
plt.imshow(imgAzul )
plt.title("Canal Azul")

Grafico.add_subplot(1,4,3)
plt.imshow(imgVerde )
plt.title("Canal Verde")

Grafico.add_subplot(1,4,4)
plt.imshow(imgVermelho )
plt.title("Canal Vermelho")

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

