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
NomeJanela = "Imagem Base"
NomeImagem  = "Pessoa.jpg"
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
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.3, fy=0.3, interpolation = cv.INTER_AREA)

# 
########################################################################
# Executando o Flip Horizontal
########################################################################
#
imgFlip = cv.flip(imgReduzida, 1)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgFlip = cv.cvtColor(imgFlip, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,2,1)
plt.imshow(imgReduzida )
plt.title("Original")

Grafico.add_subplot(1,2,2)
plt.imshow(imgFlip )
plt.title("Flip Horizontal")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
