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
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_GRAYSCALE)
imgBase = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)

# 
########################################################################
# Calculando o Limiar Médio
########################################################################
#
imgAresta = cv.Canny(imgBase,100,200)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
imgAresta = cv.cvtColor(imgAresta, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,2,1)
plt.imshow(imgBase )
plt.title("Original")

Grafico.add_subplot(1,2,2)
plt.imshow ( imgAresta )
plt.title("Detecção de Arestas")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
