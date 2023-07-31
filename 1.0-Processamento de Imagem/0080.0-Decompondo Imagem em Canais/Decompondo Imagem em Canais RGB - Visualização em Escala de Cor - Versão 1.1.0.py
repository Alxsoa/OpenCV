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
from pathlib import Path

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Lapis.jpg"
NomeDiagrama = "DiagramaRGB.png"
dirRaiz = Path.home()
dirBase = "OpenCV/"
dirImagem = "Imagens/"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoDiagrama = str(Path(dirRaiz, dirBase, dirImagem, NomeDiagrama))
dirSaida = str(Path(dirRaiz, dirBase, dirImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemColorida = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
ImgDiagrama = cv.imread ( dirCaminhoDiagrama, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemColorida is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

if ImgDiagrama is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Azul, Verde, Vermelho = cv.split(ImagemColorida)

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
#
cv.imwrite( dirSaida+"/LapisAzulCMAP.png", Azul)
cv.imwrite( dirSaida+"/LapisVerdeCMAP.png", Verde)
cv.imwrite( dirSaida+"/LapisVermelhoCMAP.png", Vermelho)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,8))

Grafico.add_subplot(1,5,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(1,5,2)
plt.imshow(ImgDiagrama )
plt.axis ( "off")
plt.title("Diagrama RGB")

Grafico.add_subplot(1,5,3)
plt.imshow(Azul, cmap="Blues" )
plt.title("Canal Azul")

Grafico.add_subplot(1,5,4)
plt.imshow(Verde, cmap="Greens" )
plt.title("Canal Verde")

Grafico.add_subplot(1,5,5)
plt.imshow(Vermelho, cmap="Reds" )
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

