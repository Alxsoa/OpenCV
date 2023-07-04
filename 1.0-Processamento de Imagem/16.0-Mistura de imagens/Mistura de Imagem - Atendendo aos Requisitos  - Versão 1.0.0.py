# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Misturada"
NomeFundo = "Oceano.jpg"
NomeFrente  = "Peixes.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemFundo = cv.imread ( CaminhoImagem + NomeFundo, cv.IMREAD_COLOR)
ImagemFundo = cv.resize ( ImagemFundo, (500, 500) , interpolation = cv.INTER_AREA)

# 
########################################################################
# Lendo a Imagem Fundo
########################################################################
#
ImagemFrente = cv.imread ( CaminhoImagem + NomeFrente, cv.IMREAD_COLOR)
ImagemFrente = cv.resize( ImagemFrente, (500, 500) , interpolation = cv.INTER_AREA)

# 
########################################################################
# Checa se Tem o Mesmo Tamanho
########################################################################
#
AlturaFrente, LarguraFrente, CanaisFrente = ImagemFrente.shape
AlturaFundo, LarguraFundo, CanaisFundo = ImagemFundo.shape

if ( (AlturaFrente==AlturaFundo) & (LarguraFrente==LarguraFundo) & (CanaisFrente==CanaisFundo)):
    print ( "########################################################################" )
    print ( "# Imagens Atendem aos Requisitos ")
    print ( "########################################################################" )    
else:
    print ( "########################################################################" )
    print ( "# Imagens NÃO Atendem aos Requisitos ")
    print ( "########################################################################" )    
    exit ()

# 
########################################################################
# Misturando a Imagem
########################################################################
#
ImagemMisturada = cv.addWeighted(ImagemFrente,0.7,ImagemFundo,0.3,0)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemFundo = cv.cvtColor(ImagemFundo, cv.COLOR_BGR2RGB)
ImagemFrente = cv.cvtColor(ImagemFrente, cv.COLOR_BGR2RGB)
ImagemMisturada = cv.cvtColor(ImagemMisturada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,6))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,3,1)
plt.imshow(ImagemFundo )
plt.axis("off")
plt.title("Oceano")

Grafico.add_subplot(1,3,2)
plt.imshow(ImagemFrente )
plt.axis("off")
plt.title("Peixes")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemMisturada )
plt.axis("off")
plt.title("Imagens\nCombinadas")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

