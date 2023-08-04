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

# 
########################################################################
# Funções de Apoio
########################################################################
#
def EfeitoPencilSketchCinza ( imgTemporario ):
    SketchCinza, SketchColorido = cv.pencilSketch (
                                                    imgTemporario, 
                                                    sigma_s=60, 
                                                    sigma_r=0.07, 
                                                    shade_factor=0.1
                                                  ) 
    return  (SketchCinza)

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
NomeOutput = "EfeitoPencilSketchCinza.jpg"
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
imgSketch = EfeitoPencilSketchCinza ( imgReduzida )
imgSketch = cv.cvtColor ( imgSketch, cv.COLOR_BGR2RGB )
# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgTodasImagens = np.hstack(( imgReduzida, imgSketch ))   

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
