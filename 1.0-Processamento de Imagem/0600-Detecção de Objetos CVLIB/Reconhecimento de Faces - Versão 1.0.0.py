# Referencia
# website: https://www.arunponnusamy.com
# https://github.com/arunponnusamy/cvlib/tree/master/examples
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cvlib as clb
import sys
import cv2 as cv
import os 

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Amigos.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
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
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgBase = cv.resize(imgBase, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Reconhecimento e Loop para Desenho do Box
########################################################################
#
Face, Confianca = clb.detect_face(imgBase)
for iFace,iConfianca in zip(Face,Confianca):

    (ptsXInicial,ptsYInicial) = iFace[0],iFace[1]
    (ptsXFinal,ptsYFinal) = iFace[2],iFace[3]

    cv.rectangle(imgBase, (ptsXInicial,ptsYInicial), (ptsXFinal,ptsYFinal), (0,255,0), 2)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#      
cv.imshow("Reconhecimento de Face", imgBase)
cv.waitKey()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################