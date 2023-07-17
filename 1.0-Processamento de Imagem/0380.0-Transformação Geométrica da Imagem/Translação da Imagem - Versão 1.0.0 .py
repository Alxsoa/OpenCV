# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "Mulher.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)

# 
########################################################################
# Recuperando Dados da Imagem
########################################################################
#
Linhas, Colunas, Canais = imgReduzida.shape

# 
########################################################################
# Definindo a Translação
# np.float32([[1,0,tx],[0,1,ty]]) 
# tx e ty Definem a translação
########################################################################
#
tEsquerda = np.float32([[1,0,-50],[0,1,0]])
tDireita  = np.float32([[1,0,50],[0,1,0]])
tSuperior = np.float32([[1,0,0],[0,1,50]])
tInferior = np.float32([[1,0,0],[0,1,-50]])

# 
########################################################################
# Translação da Imagem
# (Colunas, Linhas) Define onde ficará a imagem
########################################################################
#
imgEsquerda = cv.warpAffine(imgReduzida,tEsquerda,(Colunas, Linhas))
imgDireita  = cv.warpAffine(imgReduzida,tDireita, (Colunas, Linhas))
imgSuperior = cv.warpAffine(imgReduzida,tSuperior,(Colunas, Linhas))
imgInferior = cv.warpAffine(imgReduzida,tInferior,(Colunas, Linhas))

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgEsquerda = cv.cvtColor (imgEsquerda, cv.COLOR_BGR2RGB)
imgDireita  = cv.cvtColor (imgDireita,  cv.COLOR_BGR2RGB)
imgSuperior = cv.cvtColor (imgSuperior, cv.COLOR_BGR2RGB)
imgInferior = cv.cvtColor (imgInferior, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(11,8))

Grafico.add_subplot(2,2,1)
plt.imshow(imgEsquerda )
plt.title("Translação Esquerda", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgDireita )
plt.title("Translação Direita", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(imgSuperior )
plt.title("Translação Superior", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgInferior )
plt.title("Translação Inferior", fontsize=11, weight='bold' )

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.2,
                      hspace = 0.2 )
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
