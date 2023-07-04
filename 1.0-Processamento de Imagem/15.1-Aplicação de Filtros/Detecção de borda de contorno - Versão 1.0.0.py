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
NomeJanela = "Imagem Base"
NomeImagem  = "Mesa.jpg"
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
# Construindo a Matriz (Kernel)
########################################################################
#
matKernel = np.array([
                        [-1, -1, -1],
                        [-1,  8, -1],
                        [-1, -1, -1]
                     ]) 

########################################################################
# Aplicando o Filtro (Desfocando uma Imagem)
########################################################################
#
imgResultado = cv.filter2D(imgReduzida, -1, matKernel)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#

Grafico = plt.figure(figsize=(10,6))

Grafico.add_subplot(1,2,1)
plt.imshow ( imgReduzida )
plt.title ( "Imagem Original", fontsize=11, weight="bold" )

Grafico.add_subplot(1,2,2)
plt.imshow ( imgResultado )
plt.title ( "Imagem Filtrada", fontsize=11, weight="bold" )

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.1 )
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
