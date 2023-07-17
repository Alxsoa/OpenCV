# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import sys

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Recuperando os Dados da Imagem
########################################################################
#
ImagemAltura = Imagem.shape[0]
ImagemLargura  = Imagem.shape[1]
ImagemNumCanais = Imagem.shape[2]

# 
########################################################################
# Apresentando os Dados da Imagem
########################################################################
#
print ("")
print ("#######################################################################")
print ("# Dados da Imagem : " + NomeImagem)
print ("#######################################################################")
print ("# Largura da Imagem (pixel) ..: ", ImagemLargura )
print ("# Altura da Imagem (pixel) ...: ", ImagemAltura )
print ("# Número de Canais ...........: ", ImagemNumCanais )
print ("#######################################################################")
print ("")

########################################################################
# FIM DO PROGRAMA
########################################################################
