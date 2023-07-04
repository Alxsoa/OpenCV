import cv2 as cv
import numpy as np
  
# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela  = "Detecção de Objetos"
NomeImagem  = "TodosObjetos.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Transformando em Tons de Cinza a Imagem
########################################################################
#
ImagemBase  = cv.imread(CaminhoImagem+NomeImagem)
ImagemCinza = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Para Ser Imune a Cor do Objeto Foi Usado o Threshold Adaptativo
########################################################################
#
Threshold   = cv.adaptiveThreshold(ImagemCinza,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)  
ListaContorno, _ = cv.findContours(Threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
iAux = 0

# 
########################################################################
# lista para Armazenar os Nomes dos Objetos
########################################################################
#  
for Contorno in ListaContorno:
  
# 
########################################################################
# Ignorando o Primeiro Contador pois a Função findcontour detecta a 
# imagem Inteira como Forma
########################################################################
#  
    if iAux == 0:
        iAux = 1
        continue

# 
########################################################################
# Aproximação ao Objeto e Desenho do Contorno
########################################################################
#    
    ValorAproximado = cv.approxPolyDP(Contorno, 0.01 * cv.arcLength(Contorno, True), True)
    cv.drawContours(ImagemBase, [Contorno], 0, (0, 0, 0), 5)
  
# 
########################################################################
# Calculando o Centro do Objeto
########################################################################
#
    Momento = cv.moments(Contorno)
    if Momento['m00'] != 0.0:
        x = int(Momento['m10']/Momento['m00'])
        y = int(Momento['m01']/Momento['m00'])
  
# 
########################################################################
# Traçando a Classificação no Centro do Objeto
########################################################################
#
    if len(ValorAproximado) == 3:
        cv.putText (ImagemBase, 'Triangulo', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 128), 2)
  
    elif len(ValorAproximado) == 4:
        cv.putText (ImagemBase, 'Quadrilatero', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 128), 2)

    elif len(ValorAproximado) == 5:
        cv.putText (ImagemBase, 'Pentagono', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 128), 2)

    elif len(ValorAproximado) == 6:
        cv.putText (ImagemBase, 'Hexagono', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 128), 2)
  
    else:
        cv.putText (ImagemBase, 'Circulo', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 128), 2)
  
# 
########################################################################
# Apresentando a Imagem
########################################################################
#
#cv.imshow(NomeJanela, ImagemBase)
cv.imshow ( "JanelaBase", ImagemBase)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################