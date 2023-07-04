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
ImagemRuido = 'CaravelaRuidoSalPimenta.jpg'
NomeImagem  = "Caravela.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" + NomeImagem
CaminhoImagemRuido = CaminhoBase + "Imagens/" + ImagemRuido
EscalaPercentual = 0.80

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem, cv.IMREAD_COLOR)
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
# Inserindo o Ruído 
########################################################################
#
RuidoSalPimenta = np.zeros((ImagemAltura, ImagemLargura), dtype=np.uint8)
cv.randu(RuidoSalPimenta,0,255)
RuidoSalPimenta = cv.merge((RuidoSalPimenta,RuidoSalPimenta,RuidoSalPimenta))
RuidoSalPimenta = cv.threshold(RuidoSalPimenta,245,255,cv.THRESH_BINARY)[1]

# 
########################################################################
# Recuperando as Dimensões da Imagem com Ruido
########################################################################
#
RuidoAltura  = RuidoSalPimenta.shape[0]
RuidoLargura = RuidoSalPimenta.shape[1]
RuidoCanais  = RuidoSalPimenta.shape[2]

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
ImagemResultado = cv.add ( imgCaravela, RuidoSalPimenta ) 

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
imgCaravela = cv.cvtColor ( imgCaravela, cv.COLOR_BGR2RGB )
RuidoSalPimenta = cv.cvtColor ( RuidoSalPimenta, cv.COLOR_BGR2RGB )
ImagemResultado = cv.cvtColor ( ImagemResultado, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))
plt.title( "Transição das Imagens", fontsize=20, weight='bold' )
plt.axis ( "off" )

Grafico.add_subplot(1,3,1)
plt.imshow(imgCaravela )
plt.axis("off")
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(RuidoSalPimenta )
plt.axis("off")
plt.title("Ruído \n Sal e Pimenta")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemResultado )
plt.axis("off")
plt.title("Imagens \n Combinadas")
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

