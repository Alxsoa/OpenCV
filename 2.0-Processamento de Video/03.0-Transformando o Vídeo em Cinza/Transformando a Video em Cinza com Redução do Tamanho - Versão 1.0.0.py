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
NomeJanela = "Vídeo Transformado em Tons de Cinza"
NomeVideo  = "Escritorio.mp4"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoVideo = CaminhoBase + "Videos/"  

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo+NomeVideo)
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Mensagem de Erro ")
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = Video.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame  = Video.get(cv.CAP_PROP_FRAME_HEIGHT)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
EscalaPercentual = 0.5 
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

    ImagemCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)
    ImagemCinza = cv.resize(ImagemCinza, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
    cv.imshow ( "JanelaBase", ImagemCinza)
    cv.setWindowTitle("JanelaBase", NomeJanela )
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break

# 
########################################################################
# Fechamento dos Arquivos
########################################################################
#
cv.waitKey(0)
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
