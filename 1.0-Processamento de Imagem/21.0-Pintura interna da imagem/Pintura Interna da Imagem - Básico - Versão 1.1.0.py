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
NomeJanela  = "Imagem Base"
ImagemMascara = "PikachuMascara.png"
ImagemRiscada = "PikachuRiscado.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgMascara = cv.imread ( CaminhoImagem + ImagemMascara, cv.IMREAD_GRAYSCALE)
imgRiscada = cv.imread ( CaminhoImagem + ImagemRiscada, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgMascara is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", ImagemMascara)
    exit ()

if imgRiscada is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", ImagemRiscada)
    exit ()

# 
########################################################################
# Aplicando a Técnica Inpaint (Preenchimento por semelhança dos vizinhos)
########################################################################
#
imgRestaurada = cv.inpaint(imgRiscada, imgMascara, 3, cv.INPAINT_TELEA)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgRiscada = cv.cvtColor(imgRiscada, cv.COLOR_BGR2RGB)
imgMascara = cv.cvtColor(imgMascara, cv.COLOR_BGR2RGB)
imgRestaurada = cv.cvtColor(imgRestaurada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,3,1)
plt.imshow(imgRiscada )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(imgMascara )
plt.title("Máscara")

Grafico.add_subplot(1,3,3)
plt.imshow(imgRestaurada )
plt.title("Imagem\nRestaurada")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
