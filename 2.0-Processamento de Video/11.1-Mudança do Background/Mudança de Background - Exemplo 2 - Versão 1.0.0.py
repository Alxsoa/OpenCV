# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
#from progress.bar import Bar
import os
import platform


# 
########################################################################
# Documentação
########################################################################
#
strDoc = "\
########################################################################\n\
# Documentação do Módulo\n\
########################################################################\n\
# \n\
# Objetivo\n\
# --------\n\
# Alterar o fundo de um vídeo para uma imagem pré-determinada.\n\
# \n\
# Referencia\n\
# ----------\n\
# Não Aplicado.\n\
# \n\
# Versão das Bibliotecas Utilizadas\n\
# ---------------------------------\n\
# OpenCV ...: {0} \n\
# Numpy ....: {1} \n\
# \n\
# Versão do Ambiente\n\
# ------------------\n\
# Python ...: {2} \n\
# SO .......: {3} \n\
# \n\
########################################################################\n\
"

# 
########################################################################
# Definições Gerais
########################################################################
#
ClearCmd = "clear"  # Em Ambiente Windows deve ser usado cls
DirBase = "LocalCV/"
NomeJanela = "Video Base"
NomeVideo  = "VideoSinteticoFundoEstatico.avi"
NomeImagem = "Pessoa.jpg"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoVideo = CaminhoBase + "Videos/" 
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo+NomeVideo)
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit()

# 
########################################################################
# Recuperando os Dados do Video
########################################################################
#
LarguraFrame = Video.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame  = Video.get(cv.CAP_PROP_FRAME_HEIGHT)

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemPessoa = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Lendo o Video
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

# 
########################################################################
# Alterando o Tamanho do Frame de Video
########################################################################
#
    VideoFrame = cv.resize(VideoFrame, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Recuperando os Dados da Imagem
########################################################################
#
    Altura = VideoFrame.shape[0]
    Largura = VideoFrame.shape[1]
    Dimensao = (Largura,Altura)

    ImagemPessoaReduzida = cv.resize(ImagemPessoa, Dimensao, interpolation = cv.INTER_AREA)
#    imgPessoa = cv.cvtColor(ImagemPessoaReduzida, cv.COLOR_BGR2RGB)    

# 
########################################################################
# Adicionando o Circulo no Background
########################################################################
#
    Mascara = ImagemPessoaReduzida-VideoFrame
    Resultado = ImagemPessoaReduzida.copy ()
    Resultado[Mascara!=0] = ImagemPessoaReduzida[Mascara!=0]

    cv.imshow ( "JanelaBase", Resultado)
    cv.setWindowTitle("JanelaBase", NomeJanela )

    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break
  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################