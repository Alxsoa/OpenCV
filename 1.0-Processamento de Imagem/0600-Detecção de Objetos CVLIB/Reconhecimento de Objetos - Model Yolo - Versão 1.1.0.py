# Referencia
# website: https://www.arunponnusamy.com

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cvlib as clb
from cvlib.object_detection import draw_bbox
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
NomeImagem  = "PessoaAnimais.jpg"
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
# Executando a Identificação dos Objetos
########################################################################
#
bbox, label, conf = clb.detect_common_objects(imgBase, confidence=0.4, model="yolov5")
os.system ("clear")
print ("########################################################################")
print ("# Resumo da Detecção ")
print ("########################################################################")
print ( "Posição dos Objetos ......: ", bbox )
print ( "Descrição do Objeto ......: ", label )
print ( "Confiança de detecção ....: ", conf)
print ("########################################################################")
imgResultado = draw_bbox(imgBase, bbox, label, conf)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#     
cv.imshow("Reconhecendo Objetos", imgResultado)
cv.waitKey()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
