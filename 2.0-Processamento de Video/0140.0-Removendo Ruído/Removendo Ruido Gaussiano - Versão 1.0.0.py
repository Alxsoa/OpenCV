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
NomeJanela   = "Video Base"
NomeVideoIN  = "BaloesRuidoGaussiano.avi"
NomeVideoOUT = "BaloesSemRuidoGaussiano.avi"
CaminhoBase  = "/home/asoares/OpenCV/"
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Lendo o Video
########################################################################
#
VideoIN = cv.VideoCapture (CaminhoVideo+NomeVideoIN)
if (VideoIN.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = int(VideoIN.get(3)/2)
AlturaFrame  = int(VideoIN.get(4)/2)
size = (LarguraFrame, AlturaFrame)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOUT = cv.VideoWriter(CaminhoVideo+NomeVideoOUT,
                         cv.VideoWriter_fourcc(*'MJPG'),
                         24, size)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
VideoArray = []
print ("########################################################################")
print ("# Geração do Vídeo sem Ruído")
print ("########################################################################")
print ("# Início do Processamento de Remoção do Ruído do Vídeo ")
while(VideoIN.isOpened()):
  Status, VideoFrame = VideoIN.read()
  if Status == True:
    imgBaloes = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)    
    ImagemSemRuido = cv.fastNlMeansDenoisingColored (imgBaloes,None, 3, 3, 7, 21)
    VideoArray.append(ImagemSemRuido)

#    cv.imshow('Frame',ImagemSemRuido)
#    if cv.waitKey(25) & 0xFF == ord('q'):
#      break
 
  else: 
    break

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
print ("# Fim do Processamento de Remoção do Ruído do Vídeo ")
print ("# Início da Geração do Vídeo ")

for iAux in range (0, len(VideoArray)):
    VideoOUT.write(VideoArray[iAux])

# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
VideoIN.release()
VideoOUT.release()

print ("# Fim da Geração do Vídeo ")
print ("########################################################################")
#cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
