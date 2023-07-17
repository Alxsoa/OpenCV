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
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "PlacaNumeros.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_GRAYSCALE )
imgPlaca = cv.resize ( imgBase, (0,0), fx=0.6, fy=0.6, interpolation = cv.INTER_AREA )

# 
########################################################################
# Exemplo Básico do Uso de Limite 
########################################################################
#
th, imgPlacaBasico = cv.threshold(imgPlaca, 0, 255, cv.THRESH_BINARY)

# 
########################################################################
# Limite com o maxValues definido para 128
########################################################################
#
th, imgPlaca128 = cv.threshold ( imgPlaca, 0, 128, cv.THRESH_BINARY )

# 
########################################################################
# Limite com o maxValues definido para 128
########################################################################
#
th, imgPlaca127 = cv.threshold(imgPlaca,127,255, cv.THRESH_BINARY); 

# 
########################################################################
# Limite Usando THRESH_BINARY_INV
########################################################################
#
th, imgPlacaInv = cv.threshold(imgPlaca,127,255, cv.THRESH_BINARY_INV)

# 
########################################################################
# Limite Usando THRESH_TRUNC
########################################################################
#
th, imgPlacaTrunc = cv.threshold(imgPlaca,127,255, cv.THRESH_TRUNC)

# 
########################################################################
# Limite Usando THRESH_TRUNC
########################################################################
#
th, imgPlacaToZeros = cv.threshold(imgPlaca,127,255, cv.THRESH_TOZERO)

# 
########################################################################
# Limite Usando THRESH_TOZERO_INV
########################################################################
#
th, imgPlacaToZerosInv = cv.threshold(imgPlaca,127,255, cv.THRESH_TOZERO_INV)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgPlaca = cv.cvtColor (imgPlaca, cv.COLOR_BGR2RGB)
imgPlacaBasico  = cv.cvtColor (imgPlacaBasico,  cv.COLOR_BGR2RGB)
imgPlaca128 = cv.cvtColor (imgPlaca128, cv.COLOR_BGR2RGB)
imgPlaca127 = cv.cvtColor (imgPlaca127, cv.COLOR_BGR2RGB)
imgPlacaInv = cv.cvtColor (imgPlacaInv, cv.COLOR_BGR2RGB)
imgPlacaTrunc  = cv.cvtColor (imgPlacaTrunc,  cv.COLOR_BGR2RGB)
imgPlacaToZeros = cv.cvtColor (imgPlacaToZeros, cv.COLOR_BGR2RGB)
imgPlacaToZerosInv = cv.cvtColor (imgPlacaToZerosInv, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(11,8))

Grafico.add_subplot(2,4,1)
plt.imshow(imgPlaca )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,2)
plt.imshow(imgPlacaBasico )
plt.title("Thresold Básico", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,3)
plt.imshow(imgPlaca128 )
plt.title("Thresold maxValue 128", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,4)
plt.imshow(imgPlaca127 )
plt.title("Thresold maxValue 127", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,5)
plt.imshow(imgPlacaInv )
plt.title("Thresold THRESH_BINARY_INV", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,6)
plt.imshow(imgPlacaTrunc )
plt.title("Thresold THRESH_TRUNC", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,7)
plt.imshow(imgPlacaToZeros )
plt.title("Thresold THRESH_TOZERO", fontsize=11, weight='bold' )

Grafico.add_subplot(2,4,8)
plt.imshow(imgPlacaToZerosInv )
plt.title("Thresold THRESH_TOZERO_INV", fontsize=11, weight='bold' )

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
