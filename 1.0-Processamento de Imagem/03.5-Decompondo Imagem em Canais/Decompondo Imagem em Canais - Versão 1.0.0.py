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
ImagemColorida = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
ImagemColorida = cv.resize ( ImagemColorida, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Azul, Verde, Vermelho = cv.split(ImagemColorida)

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
#
cv.imwrite( CaminhoImagem+"GirassolAzul.png", Azul)
cv.imwrite( CaminhoImagem+"GirassolVerde.png", Verde)
cv.imwrite( CaminhoImagem+"GirassolVermelho.png", Vermelho)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgAzul = cv.cvtColor(Azul, cv.COLOR_BGR2RGB)
imgVerde = cv.cvtColor(Verde, cv.COLOR_BGR2RGB)
imgVermelho = cv.cvtColor(Vermelho, cv.COLOR_BGR2RGB)

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
plt.title("Original")

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

