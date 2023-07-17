# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela  = "Reconhecimento Padrao"
NomePadrao  = "haarcascade_frontalcatface.xml"
NomeImagem  = "FotoGato.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoPadrao= CaminhoBase + "Padroes/" 
CaminhoImagem= CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo o Padrão de Reconhecimento
########################################################################
#
CascataFaces = cv.CascadeClassifier(CaminhoPadrao+NomePadrao)

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Loop de Busca do Padrão
########################################################################
#
ImagemCinza = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)
Faces = CascataFaces.detectMultiScale(ImagemCinza, 1.1, 3)
print( "Número de Faces Detectadas = ", len(Faces))

if len(Faces) > 0:
   for (x,y,w,h) in Faces:

      cv.rectangle(ImagemBase,(x,y),(x+w,y+h),(0,255,255),2)
      cv.putText(ImagemBase, "Face Felina", (x, y-3), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

# 
########################################################################
# Apresentando a Imagem Cinza
########################################################################
#
cv.imshow('Reconhecimento Padrao',ImagemBase)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
