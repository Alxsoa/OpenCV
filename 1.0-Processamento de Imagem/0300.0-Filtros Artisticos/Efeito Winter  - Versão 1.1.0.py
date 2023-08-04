# Referencia
# https://www.analyticsvidhya.com/blog/2021/07/an-interesting-opencv-application-creating-filters-like-instagram-and-picsart/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import numpy as np
from pathlib import Path
from scipy.interpolate import UnivariateSpline

# 
########################################################################
# Funções de Apoio
########################################################################
#
def LookupTable(x, y):
  spline = UnivariateSpline(x, y)
  return spline(range(256))

def EfeitoWinter ( imgTemporario ):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel = cv.split(imgTemporario)
    red_channel = cv.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win = cv.merge((blue_channel, green_channel, red_channel))
    return (win)


def LimpaTerminal ():
    if os.name == "nt":
       _ = os.system( "cls" )
    else:
      _ = os.system( "clear ")
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem = "Padaria.jpg"
NomeOutput = "EfeitoWinter.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirOutput = "Output"
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoOutput = str(Path(dirRaiz, dirBase, dirOutput, NomeOutput))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Aplicando o Efeito
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)
imgWinter = EfeitoWinter ( imgReduzida )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgTodasImagens = np.hstack(( imgReduzida, imgWinter))   

cv.imshow ( "Resultado Efeitos", imgTodasImagens)  
cv.waitKey(0)
cv.destroyAllWindows()

# 
########################################################################
# Armazenando o Resultado
########################################################################
#
cv.imwrite ( dirCaminhoOutput, imgTodasImagens )

########################################################################
# FIM DO PROGRAMA
########################################################################
