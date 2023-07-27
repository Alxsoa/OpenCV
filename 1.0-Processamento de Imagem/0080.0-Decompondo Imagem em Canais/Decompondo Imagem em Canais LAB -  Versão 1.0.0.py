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
NomeDiagrama = "DiagramaLAB.jpg"
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
# Transformando para o Padrào HSV
########################################################################
#
imgRGB = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgLAB = cv.cvtColor(imgRGB, cv.COLOR_RGB2LAB)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
L, A, B = cv.split(imgLAB)

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
#
cv.imwrite( CaminhoImagem+"GirassolLABL.png", L)
cv.imwrite( CaminhoImagem+"GirassolLABA.png", A)
cv.imwrite( CaminhoImagem+"GirassolLABB.png", B)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgL = cv.cvtColor(L, cv.COLOR_BGR2RGB)
imgA = cv.cvtColor(A, cv.COLOR_BGR2RGB)
imgB = cv.cvtColor(B, cv.COLOR_BGR2RGB)

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
plt.title("Diagrama LAB")

Grafico.add_subplot(1,5,3)
plt.imshow(imgL )
plt.title("Canal Lightness")

Grafico.add_subplot(1,5,4)
plt.imshow(imgA )
plt.title("Canal A")

Grafico.add_subplot(1,5,5)
plt.imshow(imgB )
plt.title("Canal B")

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

