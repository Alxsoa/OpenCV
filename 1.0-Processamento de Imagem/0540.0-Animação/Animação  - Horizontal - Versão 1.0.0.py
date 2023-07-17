# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Exemplo de Animação"
NomeImagem  = "Pessoa.jpg"
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
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
Altura, Largura, Canais = imgReduzida.shape
iAux = 0
  
while True:
    iAux += 1

# 
########################################################################
# Dividimos a imagem em partes esquerda e direita    
########################################################################
#      
    MatrizEsquerda = imgReduzida[:, :(iAux % Largura)]
    MatrizDireita  = imgReduzida[:, (iAux % Largura):]

# 
########################################################################
# Concatenação da Matriz Direita e Esquerda       
########################################################################
#    
    imgResultado = np.hstack((MatrizDireita, MatrizEsquerda))
      
# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
    cv.imshow ( "JanelaBase", imgResultado)
    cv.setWindowTitle("JanelaBase", NomeJanela )     
    if cv.waitKey(1) == ord('q'):
       cv.destroyAllWindows()
       break

########################################################################
# FIM DO PROGRAMA
########################################################################
