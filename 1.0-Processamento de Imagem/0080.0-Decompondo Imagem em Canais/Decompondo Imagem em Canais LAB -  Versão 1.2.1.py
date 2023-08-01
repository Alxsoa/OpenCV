# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os
from pathlib import Path

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Lapis.jpg"
NomeDiagrama = "DiagramaLAB.jpg"
dirRaiz = Path.home()
dirBase = "OpenCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoDiagrama = str(Path(dirRaiz, dirBase, dirImagem, NomeDiagrama))
dirSaida = str(Path(dirRaiz, dirBase, dirImagem))

dirSaidaCanal1 = str(Path(dirRaiz, dirBase, dirImagem, "LapisLABL.png"))
dirSaidaCanal2 = str(Path(dirRaiz, dirBase, dirImagem, "LapisLABA.png"))
dirSaidaCanal3 = str(Path(dirRaiz, dirBase, dirImagem, "LapisLABB.png"))

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
    print( "Não Foi Localizada a Imagem : ", NomeDiagrama)
    exit ()

# 
########################################################################
# Transformando para o Padrào HSV
########################################################################
#
imgLAB = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2LAB)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
L, A, B = cv.split(imgLAB)

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
cv.imwrite( dirSaidaCanal1, L)
cv.imwrite( dirSaidaCanal2, A)
cv.imwrite( dirSaidaCanal3, B)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgL = cv.cvtColor(L, cv.COLOR_BGR2RGB)
imgA = cv.cvtColor(A, cv.COLOR_BGR2RGB)
imgB = cv.cvtColor(B, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(16,8))

Grafico.add_subplot(1,5,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(1,5,2)
plt.imshow(ImgDiagrama )
plt.axis ( "off")
plt.title("Diagrama LAB")

Grafico.add_subplot(1,5,3)
plt.imshow(imgL )
plt.title("Canal Lightness")

Grafico.add_subplot(1,5,4)
plt.imshow(imgA )
plt.title("Canal A")

Grafico.add_subplot(1,5,5)
plt.imshow(imgB )
plt.title("Canal B")

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.2,
                      hspace = 0.1 )

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

