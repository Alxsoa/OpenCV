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
def EfeitoSepia ( imgTemporario ):
    # convertendo para float para evitar perdas
    imgTemporario = np.array(imgTemporario, dtype=np.float64) 

    Matriz = np.matrix ([
                            [0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]
                        ])
    
    # multiplicando a imagem com matriz sépia 
    imgTemporario = cv.transform ( imgTemporario, Matriz ) 

    # normalizando valores maiores que 255 a 255
    imgTemporario[np.where(imgTemporario > 255)] = 255 
    imgTemporario = np.array(imgTemporario, dtype=np.uint8)
    return (imgTemporario)

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
NomeOutput = "EfeitoSepia.jpg"
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
imgSepia = EfeitoSepia ( imgReduzida )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgTodasImagens = np.hstack(( imgReduzida, imgSepia))   

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
