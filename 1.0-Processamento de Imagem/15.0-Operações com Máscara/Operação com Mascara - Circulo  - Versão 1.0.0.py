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
# Construindo a Matriz 
########################################################################
#
Largura = imgReduzida.shape[0]
Altura  = imgReduzida.shape[1]
imgRecorte = np.zeros( (Largura, Altura), dtype="uint8")
#imgRecorte = np.zeros(imgReduzida.shape[:2], dtype="uint8")
imgAuxiliar = imgRecorte.copy()

# 
########################################################################
# Criando a Máscara
########################################################################
#
Mascara = cv.circle(imgRecorte, (300, 160), 150, 255, -1)

# 
########################################################################
# Aplicando a Máscara
########################################################################
#
imgResultado = cv.bitwise_and (imgReduzida, imgReduzida, mask= Mascara)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgAuxiliar = cv.cvtColor(imgAuxiliar, cv.COLOR_BGR2RGB)
Mascara = cv.cvtColor(Mascara, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(2,2,1)
plt.imshow(imgReduzida )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgAuxiliar )
plt.title("Imagem Recorte", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(Mascara )
plt.title("Imagem Máscara", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgResultado )
plt.title("Imagem Resultado", fontsize=11, weight='bold' )

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
