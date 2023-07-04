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
NomeVideo = "Escritorio.mp4"
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
        Azul, Verde, Vermelho = cv.split(VideoFrame)
        imgAzul  = cv.resize(Azul, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
        imgVerde = cv.resize(Verde, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
        imgVermelho = cv.resize(Vermelho, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
        imgVideoFrame = cv.resize(VideoFrame, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
        cv.imshow ( "Canal Azul", imgAzul)
        cv.imshow ( "Canal Verde", imgVerde)
        cv.imshow ( "Canal Vermelho", imgVermelho)
        cv.imshow ( "Video Original", imgVideoFrame)

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
