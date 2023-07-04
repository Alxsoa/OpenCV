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
NomeJanela = "Video Base"
NomeVideo = "Baloes.mp4"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoVideo= CaminhoBase + "Videos/" 

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo + NomeVideo)
if (Video.isOpened()== False): 
  print ("########################################################################")
  print ("# Video Não Encontrado ")
  print ("########################################################################")
  exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = int(Video.get(3)/2)
AlturaFrame  = int(Video.get(4)/2)
size = (LarguraFrame, AlturaFrame)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter(CaminhoVideo+'BaloesRuidoSalPimenta.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         24, size)
 
# 
########################################################################
# Apresentando o Vídeo Com Redução
########################################################################
#
print ("########################################################################")
print ("# Geração do Vídeo com Ruído")
print ("########################################################################")
print ("# Início da Geração do Vídeo ")
VideoArray = []
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
 
    imgBaloes = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)
# 
########################################################################
# Recuperando as Dimensões da Imagem 
########################################################################
#
    ImagemAltura  = imgBaloes.shape[0]
    ImagemLargura = imgBaloes.shape[1]
    ImagemCanais  = imgBaloes.shape[2]

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
# Combinando as Imagens
########################################################################
#
    ImagemResultado = cv.add ( imgBaloes, RuidoSalPimenta ) 
#    cv.imshow('Video com Ruido',ImagemResultado)
    VideoArray.append(ImagemResultado)

#    if cv.waitKey(25) & 0xFF == ord('q'):
#      break
 
  else: 
    break

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(VideoArray)):
    VideoOut.write(VideoArray[iAux])
    
# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
Video.release()
print ("# Fim da Geração do Vídeo ")
print ("########################################################################")
#cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
