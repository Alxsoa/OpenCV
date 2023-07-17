# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela  = "Imagem Base"
ImagemCarro1 = "audi.jpg"
ImagemCarro2 = "Carro.jpeg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgCarro1 = cv.imread ( CaminhoImagem + ImagemCarro1, cv.IMREAD_COLOR)
imgCarro2 = cv.imread ( CaminhoImagem + ImagemCarro2, cv.IMREAD_COLOR)

# 
########################################################################
# Padronizando o Tamanho das Imagens
########################################################################
#
imgPadraoCarro1 = cv.resize(imgCarro1, (500, 500) , interpolation = cv.INTER_AREA) 
imgPadraoCarro2 = cv.resize(imgCarro2, (500, 500) , interpolation = cv.INTER_AREA) 

# 
########################################################################
# Concatenando Verticalmente as Imagens
########################################################################
#
imgConcatenada = cv.vconcat([imgPadraoCarro1, imgPadraoCarro2])
imgConcatenada = cv.cvtColor(imgConcatenada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
plt.imshow(imgConcatenada)
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
