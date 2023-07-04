# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#

import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2 as cv

# 
########################################################################
# Definições Gerais
########################################################################
#
FonteCaminho = "/home/asoares/OpenCV/1.0-Processamento de Imagem/11.0-Escrita de Texto Customizada em Imagem/"
FonteNome  = "Oswald-SemiBold.ttf"
NomeJanela = "Fonte Customizada"
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Selecionando o Fonte de Texto
########################################################################
#
font = ImageFont.truetype(FonteCaminho+FonteNome, 32)
ImagemArray = Image.fromarray(Imagem)
draw = ImageDraw.Draw(ImagemArray)

# 
########################################################################
# Escrevendo o Texto
########################################################################
#
draw.text((5, 5),  "Alinhamento\nEsquerda", font = font , align ="left", fill ="yellow") 
draw.text((450, 5),  "Alinhamento\nEsquerda", font = font , align ="right", fill ="blue") 
draw.text((250, 230),  "Alinhamento\nao Centro", font = font , align ="center", fill ="green") 
ImagemEscrita = np.array(ImagemArray)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
#cv.imshow (NomeJanela, ImagemEscrita);
cv.imshow ( "JanelaBase", ImagemEscrita)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey ();
cv.destroyAllWindows ()

########################################################################
# FIM DO PROGRAMA
########################################################################

