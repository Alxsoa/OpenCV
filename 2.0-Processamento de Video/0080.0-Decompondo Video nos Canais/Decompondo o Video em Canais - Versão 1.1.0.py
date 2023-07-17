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
BaseDir = "LocalCV/"
NomeVideo = "Escritorio.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo= CaminhoBase + "Videos/" 

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo + NomeVideo)
if (Video.isOpened()== False): 
  print ("########################################################################")
  print ("# Mensagem de Erro ")
  print ("########################################################################")
  print ("# Video Não Encontrado ")
  print ("########################################################################")
  exit()
  
# 
########################################################################
# Apresentando o Vídeo Com Redução
########################################################################
#
EscalaPercentual = 0.3
while(Video.isOpened()):
    Status, VideoFrame = Video.read()
    if Status == True:
# 
########################################################################
# Separando a Imagem nos Canais 
########################################################################
#
        VideoFrame = cv.resize(VideoFrame, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
        Azul, Verde, Vermelho = cv.split(VideoFrame)

        zeros = np.zeros(VideoFrame.shape[:2], dtype="uint8")
        Vermelho = cv.merge([zeros, zeros, Vermelho])
        Verde = cv.merge([zeros, Verde, zeros])
        Azul = cv.merge([Azul, zeros, zeros])

# 
########################################################################
# Apresentando a Imagem
########################################################################
#     
        imgLinha1 = np.hstack(( VideoFrame, Azul ))  
        imgLinha2 = np.hstack(( Verde, Vermelho ))  
        imgTodasImagens = np.vstack(( imgLinha1, imgLinha2 ))  

        cv.imshow ( "Canais da Imagem", imgTodasImagens)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
        
    else: 
        break
  
# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
