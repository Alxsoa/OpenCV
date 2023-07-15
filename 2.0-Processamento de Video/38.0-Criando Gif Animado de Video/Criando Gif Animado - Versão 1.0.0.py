# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2
import imageio
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeVideo = "Chaplin.mp4"
NomeSaida = "Chaplin.gif"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/"

# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
Video = cv2.VideoCapture( CaminhoVideo + NomeVideo )
if not Video.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

# 
########################################################################
# Loop de Criação do Gif Animado
########################################################################
#
lstFrameVideo = []
while True:
    Status, VideoFrame = Video.read()

    if Status == True:
        tmpFrame = cv2.resize(VideoFrame, (0,0), fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
        tmpFrameRGB = cv2.cvtColor(tmpFrame, cv2.COLOR_BGR2RGB)
        lstFrameVideo.append(tmpFrameRGB)
    else:
        break

# 
########################################################################
# Fechando o Video
########################################################################
#        
Video.release()

# 
########################################################################
# Salvando o Gif Animado a Duracao é em ms (50 fps == 20 duration)
########################################################################
#
imageio.mimsave( CaminhoVideo + NomeSaida, lstFrameVideo, duration=30)

########################################################################
# FIM DO PROGRAMA
########################################################################