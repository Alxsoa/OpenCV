# Referencia
# https://www.analyticsvidhya.com/blog/2021/07/an-interesting-opencv-application-creating-filters-like-instagram-and-picsart/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

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

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Padaria.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
imgReduzida = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Ajustando o Brilho
########################################################################
#
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

########################################################################
# FIM DO PROGRAMA
########################################################################
