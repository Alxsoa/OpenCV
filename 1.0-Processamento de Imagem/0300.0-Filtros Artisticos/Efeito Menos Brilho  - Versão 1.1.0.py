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
def AcertaBrilho (imgTemporario, ValorBeta ):
    imgBrilho  = cv.convertScaleAbs(imgTemporario, beta=ValorBeta)
    return (imgBrilho)

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
NomeOutput = "EfeitoMenosBrilho.jpg"
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
imgBrilho = AcertaBrilho (imgReduzida, -60)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgTodasImagens = np.hstack(( imgReduzida, imgBrilho))   

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
