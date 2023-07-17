# Referencia
# https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590
# https://docs.opencv.org/3.4/d1/d89/tutorial_py_orb.html

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2
import numpy as np
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeImagemBase = "LivroFrontalTesla.jpg"
NomeImagemComparada = "LivroInclinadoTesla.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
ImagemBase = cv2.imread ( CaminhoImagem + NomeImagemBase, cv2.IMREAD_COLOR )
ImagemComparada = cv2.imread ( CaminhoImagem + NomeImagemComparada, cv2.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemBase)
    exit ()

if ImagemComparada is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemComparada)
    exit ()

# 
########################################################################
# Executa a Correlação
########################################################################
#
orbDetector = cv2.ORB_create(nfeatures=1500)
ptsPrincipal1, Descritor1 = orbDetector.detectAndCompute(ImagemBase, None)
ptsPrincipal2, Descritor2 = orbDetector.detectAndCompute(ImagemComparada, None)

bfDetector = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
Correspondencias = bfDetector.match(Descritor1, Descritor2)
Correspondencias = sorted(Correspondencias, key=lambda x: x.distance)

# 
########################################################################
# apresenta os 50 Primeiros Resultados
########################################################################
#
imgResultado = cv2.drawMatches(ImagemBase, ptsPrincipal1, ImagemComparada, ptsPrincipal2, Correspondencias[:50], None)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
cv2.imshow( "Correspondencias da Imagem", imgResultado)
cv2.waitKey()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
