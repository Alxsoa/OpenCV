# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
ImagemRuido = 'CaravelaRuidoGausiano.jpg'
NomeImagem  = "Caravela.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" + NomeImagem
CaminhoImagemRuido = CaminhoBase + "Imagens/" + ImagemRuido
EscalaPercentual = 0.80

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem )
    exit ()

# 
########################################################################
# Reduzindo a Imagem
########################################################################
#
imgCaravela = cv.resize(Imagem, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual, interpolation = cv.INTER_AREA)

# 
########################################################################
# Recuperando as Dimensões da Imagem 
########################################################################
#
ImagemAltura = imgCaravela.shape[0]
ImagemLargura  = imgCaravela.shape[1]
ImagemCanais = imgCaravela.shape[2]

# 
########################################################################
# Inserindo o Ruído (Média 128 e sigma 20)
########################################################################
#
RuidoGausiano = np.zeros((ImagemAltura, ImagemLargura) )
cv.randn(RuidoGausiano,128,20)
RuidoGausiano =(RuidoGausiano*0.5).astype(np.uint8)
RuidoGausiano = cv.merge((RuidoGausiano,RuidoGausiano,RuidoGausiano))

# 
########################################################################
# Recuperando as Dimensões da Imagem com Ruido
########################################################################
#
RuidoAltura = RuidoGausiano.shape[0]
RuidoLargura = RuidoGausiano.shape[1]
RuidoCanais  = RuidoGausiano.shape[2]

# 
########################################################################
# Checando se as Imagens São do Mesmo Tamanho
########################################################################
#
print ( "########################################################################")
print ( "# Avaliando as Condições para o Merge")
print ( "########################################################################")
print ( "# Altura Imagem Original .....: ", ImagemAltura)
print ( "# Largura Imagem Original ....: ", ImagemLargura)
print ( "# Canais Imagem Original .....: ", ImagemCanais)
print ( "# ")
print ( "# Altura Imagem Ruido ........: ", RuidoAltura)
print ( "# Largura Imagem Ruido .......: ", RuidoLargura)
print ( "# Canais Imagem Ruido ........: ", RuidoCanais)
print ( "# ")

# 
########################################################################
# Combinando as Imagens
########################################################################
#
ImagemResultado = cv.add ( imgCaravela,RuidoGausiano) 

# 
########################################################################
# Salvando a Imagem com Ruído
########################################################################
#
cv.imwrite (CaminhoImagemRuido, ImagemResultado)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgCaravela = cv.cvtColor(imgCaravela, cv.COLOR_BGR2RGB)
RuidoGausiano = cv.cvtColor(RuidoGausiano, cv.COLOR_BGR2RGB)
ImagemResultado = cv.cvtColor(ImagemResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,3,1)
plt.imshow(imgCaravela )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(RuidoGausiano )
plt.title("Ruído Gausiano")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemResultado )
plt.title("Imagens \n Combinadas")

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
