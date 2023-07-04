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
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/"  

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgGirassolAzul = cv.imread ( CaminhoImagem + "GirassolAzul.png", cv.IMREAD_UNCHANGED)
imgGirassolVerde = cv.imread ( CaminhoImagem + "GirassolVerde.png", cv.IMREAD_UNCHANGED)
imgGirassolVermelho = cv.imread ( CaminhoImagem + "GirassolVermelho.png", cv.IMREAD_UNCHANGED)

# 
########################################################################
# Montando a Imagem a Partir dos Canais
########################################################################
#
ImagemColorida = cv.merge ([imgGirassolVermelho, imgGirassolVerde, imgGirassolAzul])

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
#ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgAzul = cv.cvtColor(imgGirassolAzul, cv.COLOR_BGR2RGB)
imgVerde = cv.cvtColor(imgGirassolVerde, cv.COLOR_BGR2RGB)
imgVermelho = cv.cvtColor(imgGirassolVermelho, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,4,1)
plt.imshow(ImagemColorida )
plt.title("Imagem\nReconstruída")

Grafico.add_subplot(1,4,2)
plt.imshow(imgAzul )
plt.title("Canal Azul")

Grafico.add_subplot(1,4,3)
plt.imshow(imgVerde )
plt.title("Canal Verde")

Grafico.add_subplot(1,4,4)
plt.imshow(imgVermelho )
plt.title("Canal Vermelho")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

