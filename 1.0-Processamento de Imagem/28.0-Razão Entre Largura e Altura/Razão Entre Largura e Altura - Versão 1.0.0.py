# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Funções Necessárias
########################################################################
#
def aspect_ratio(cnt):
   x, y, w, h = cv.boundingRect(cnt)
   ratio = float(w)/h
   return ratio

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Razão Entre Largura e Altura"
NomeImagem  = "LarguraAltura.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
img = cv.imread(CaminhoImagem+NomeImagem)
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Aproximação ao Objeto e Desenho do Contorno
########################################################################
# 
thresh = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,3,0) 
contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

print ("########################################################################")
print ("# Aproximação ao Objeto e Desenho do Contorno")
print ("########################################################################")
print ("# Número de Objetos ....: ", len(contours))

# 
########################################################################
# Loop para Todos os Contornos
########################################################################
#
for i, cnt in enumerate(contours):
   ar = aspect_ratio(cnt)
   ar = round(ar, 3)
   x,y,w,h = cv.boundingRect(cnt)
   cv.drawContours(img,[cnt],0,(0,255,0),2)
   cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   cv.putText(img, f'{ar}', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
   print (" Proporção do objeto ...: ", ar)
print ("########################################################################")

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", img)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
