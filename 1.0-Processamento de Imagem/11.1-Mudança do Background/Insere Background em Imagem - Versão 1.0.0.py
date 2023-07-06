# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import mediapipe as mp

# 
########################################################################
# Definições Gerais
########################################################################
#
DirBase = "OpenCV/"
NomeJanela = "Imagem Reduzida"
NomeImagemFront = "Mulher.jpg"
NomeImagemBackground = "Cena.jpg"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgFrente = cv.imread ( CaminhoImagem + NomeImagemFront, cv.IMREAD_COLOR)
imgFundo = cv.imread ( CaminhoImagem + NomeImagemBackground, cv.IMREAD_COLOR)

# 
########################################################################
# Compatibilizando o Tamanho das Imagens
########################################################################
#
imgFrente = cv.resize(imgFrente, (640, 480))
imgFundo  = cv.resize(imgFundo, (640, 480))

# 
########################################################################
# Apresentando o Resultado Parcial
########################################################################
#
cv.imshow ( "Imagem Frente", imgFrente)
cv.imshow ( "Imagem Fundo", imgFundo)

# 
########################################################################
# Segmentando a Imagem
########################################################################
#
imgSegmentada = mp.solutions.selfie_segmentation
imgSegmento = imgSegmentada.SelfieSegmentation(model_selection = 1)

# 
########################################################################
# Criando a Máscara
########################################################################
#
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_BGR2RGB)
imgResultado = imgSegmento.process(imgFrente)
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_RGB2BGR)
imgSegmentoMascara = imgResultado.segmentation_mask

# 
########################################################################
# Executando a União das Imagens
########################################################################
#
Limiar = 0.6
imgMascaraBinaria = imgSegmentoMascara > Limiar
imgMascara3d = np.dstack((imgMascaraBinaria, imgMascaraBinaria, imgMascaraBinaria))
imgResultadoFinal = np.where(imgMascara3d, imgFrente, imgFundo)

# 
########################################################################
# Apresentando o Resultado Final
########################################################################
#
cv.imshow ( "Resultado Final", imgResultadoFinal)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
