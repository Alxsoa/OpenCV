# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
NomeDiagrama = "DiagramaRGB.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/"  

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemColorida = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
ImgDiagrama = cv.imread ( CaminhoImagem + NomeDiagrama, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemColorida is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

if ImgDiagrama is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Reduzindo a Imagem
########################################################################
#
ImagemColorida = cv.resize(ImagemColorida, (300, 300), interpolation = cv.INTER_AREA)

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
Grafico = plt.figure(figsize=(16,8))

Grafico.add_subplot(1,5,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(1,5,2)
plt.imshow(ImgDiagrama )
plt.axis ( "off")
plt.title("Diagrama RGB")

Grafico.add_subplot(1,5,3)
plt.imshow(imgAzul )
plt.title("Canal Azul")

Grafico.add_subplot(1,5,4)
plt.imshow(imgVerde )
plt.title("Canal Verde")

Grafico.add_subplot(1,5,5)
plt.imshow(imgVermelho )
plt.title("Canal Vermelho")

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.2,
                      hspace = 0.1 )

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

