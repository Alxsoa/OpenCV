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
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
NomeDiagrama = "DiagramaHSV.png"
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
imgHSV = cv.cvtColor(imgRGB, cv.COLOR_RGB2HSV)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Matiz, Saturacao, Valor = cv.split(imgHSV)

# 
########################################################################
# Salvando os Canais em Arquivos Diferentes
########################################################################
#
cv.imwrite( CaminhoImagem+"GirassolHSVMatiz.png", Matiz)
cv.imwrite( CaminhoImagem+"GirassolHSVSaturacao.png", Saturacao)
cv.imwrite( CaminhoImagem+"GirassolHSVValor.png", Valor)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgMatiz = cv.cvtColor(Matiz, cv.COLOR_BGR2RGB)
imgSaturacao = cv.cvtColor(Saturacao, cv.COLOR_BGR2RGB)
imgValor = cv.cvtColor(Valor, cv.COLOR_BGR2RGB)

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
plt.title("Diagrama HSV")

Grafico.add_subplot(1,5,3)
plt.imshow(imgMatiz )
plt.title("Canal Matiz")

Grafico.add_subplot(1,5,4)
plt.imshow(imgSaturacao )
plt.title("Canal Saturacao")

Grafico.add_subplot(1,5,5)
plt.imshow(imgValor )
plt.title("Canal Intensidade")

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

