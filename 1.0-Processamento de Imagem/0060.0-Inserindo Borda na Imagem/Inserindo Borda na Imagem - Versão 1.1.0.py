# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
DirBase = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Cafeteria.png"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Reduzindo as Dimensões da Imagem
########################################################################
#
imgBase = cv.resize(imgBase, (640, 480), interpolation = cv.INTER_AREA)

# 
########################################################################
# Inserindo a Borda
########################################################################
#
imgBorda = cv.copyMakeBorder (
                                src=imgBase, 
                                top=15, 
                                bottom=15, 
                                left=15, 
                                right=15, 
                                borderType=cv.BORDER_CONSTANT, 
                                value=(255,255,255)
                             ) 

# 
########################################################################
# Apresentando a Imagem 
########################################################################
#
cv.imshow ( "Cafeteria Original", imgBase)
cv.imshow ( "Cafeteria com Borda", imgBorda)

# 
########################################################################
# Destruindo o Janelamento
########################################################################
#
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
