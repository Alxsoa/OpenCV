# Referencia
# https://www.tutorialspoint.com/how-to-compare-two-images-in-opencv-python#

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
   
# 
########################################################################
# Funções de Apoio
########################################################################
#
def CalculaErro ( imgTmpOriginal, imgTmpComparada, Altura, Largura):
    imgDiferenca = cv.subtract(imgTmpOriginal, imgTmpComparada)
    Erro = np.sum(imgDiferenca**2)
    mse = Erro/(float(Altura*Largura))
    #msre = np.sqrt(mse)
    return (mse) 

  
# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeImagem = [ "Violao1.jpg", "Violao2.jpg", "Violao3.jpg", "Violao4.jpg", "Violao5.jpg" , "Violao6.jpg"  ]
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgViolaoOriginal = cv.imread ( CaminhoImagem + NomeImagem[0], cv.IMREAD_COLOR )
if imgViolaoOriginal is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[0])
   exit ()


imgViolaoOpcao1 = cv.imread ( CaminhoImagem + NomeImagem[1], cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[1])
   exit ()

imgViolaoOpcao2 = cv.imread ( CaminhoImagem + NomeImagem[2], cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[2])
   exit ()

imgViolaoOpcao3 = cv.imread ( CaminhoImagem + NomeImagem[3], cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[3])
   exit ()

imgViolaoOpcao4 = cv.imread ( CaminhoImagem + NomeImagem[4], cv.IMREAD_COLOR )
if imgViolaoOpcao4 is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[4])
   exit ()

imgViolaoOpcao5 = cv.imread ( CaminhoImagem + NomeImagem[5], cv.IMREAD_COLOR )
if imgViolaoOpcao5 is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem[5])
   exit ()
# 
########################################################################
# Uniformizando o Tamanho das Imagens
########################################################################
#
imgViolaoOriginal = cv.resize(imgViolaoOriginal, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao1 = cv.resize(imgViolaoOpcao1, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao2 = cv.resize(imgViolaoOpcao2, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao3 = cv.resize(imgViolaoOpcao3, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao4 = cv.resize(imgViolaoOpcao4, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao5 = cv.resize(imgViolaoOpcao5, (160, 400), interpolation = cv.INTER_AREA)

# 
########################################################################
# Calculo da Diferença
########################################################################
#
DiferencaOriginalImagem1 = CalculaErro ( imgViolaoOriginal, imgViolaoOpcao1, 400, 160)
DiferencaOriginalImagem2 = CalculaErro ( imgViolaoOriginal, imgViolaoOpcao2, 400, 160)
DiferencaOriginalImagem3 = CalculaErro ( imgViolaoOriginal, imgViolaoOpcao3, 400, 160)
DiferencaOriginalImagem4 = CalculaErro ( imgViolaoOriginal, imgViolaoOpcao4, 400, 160)
DiferencaOriginalImagem5 = CalculaErro ( imgViolaoOriginal, imgViolaoOpcao5, 400, 160)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgViolaoOriginal = cv.cvtColor(imgViolaoOriginal, cv.COLOR_BGR2RGB)
imgViolaoOpcao1 = cv.cvtColor(imgViolaoOpcao1, cv.COLOR_BGR2RGB)
imgViolaoOpcao2 = cv.cvtColor(imgViolaoOpcao2, cv.COLOR_BGR2RGB)
imgViolaoOpcao3 = cv.cvtColor(imgViolaoOpcao3, cv.COLOR_BGR2RGB)
imgViolaoOpcao4 = cv.cvtColor(imgViolaoOpcao4, cv.COLOR_BGR2RGB)
imgViolaoOpcao5 = cv.cvtColor(imgViolaoOpcao5, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,14))

Grafico.add_subplot(2,3,1)
plt.imshow(imgViolaoOriginal )
plt.title("Original")

Grafico.add_subplot(2,3,2)
plt.imshow(imgViolaoOpcao1 )
plt.title('Grau de Diferença\n ({:.2f})'.format(DiferencaOriginalImagem1))

Grafico.add_subplot(2,3,3)
plt.imshow(imgViolaoOpcao2 )
plt.title('Grau de Diferença\n ({:.2f})'.format(DiferencaOriginalImagem2))

Grafico.add_subplot(2,3,4)
plt.imshow(imgViolaoOpcao3 )
plt.title('Grau de Diferença\n ({:.2f})'.format(DiferencaOriginalImagem3))

Grafico.add_subplot(2,3,5)
plt.imshow(imgViolaoOpcao4 )
plt.title('Grau de Diferença\n ({:.2f})'.format(DiferencaOriginalImagem4))

Grafico.add_subplot(2,3,6)
plt.imshow(imgViolaoOpcao5 )
plt.title('Grau de Diferença\n  ({:.2f})'.format(DiferencaOriginalImagem5))

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.3 )

plt.show ()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
