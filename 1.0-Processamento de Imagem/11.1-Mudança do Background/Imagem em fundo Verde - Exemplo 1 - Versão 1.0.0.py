
import cv2 as cv

backSub = cv.createBackgroundSubtractorKNN()
capture = cv.VideoCapture(cv.samples.findFileOrKeep("/home/asoares/OpenCV/Videos/DuasPessoasMetro.mp4"))

if not capture.isOpened():
    print('Unable to open: ' )
    exit(0)

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    frame = cv.resize(frame, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)    
    fgMask = backSub.apply(frame)
    
    
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

exit()
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
NomeJanela = "Imagem Reduzida"
FundoVerde = "PessoaFundoVerde.png"
FrenteImagem = "SecaoEleitoral.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgFundoVerde = cv.imread ( CaminhoImagem + FundoVerde, cv.IMREAD_COLOR)
imgFrenteImagem = cv.imread ( CaminhoImagem + FrenteImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Normalizando o Tamanho da Imagem
########################################################################
#
frame = cv.resize(imgFundoVerde, (640, 480))
image = cv.resize(imgFrenteImagem, (640, 480))

# 
########################################################################
# Definindo a Graduação de Verde Presente no Fundo
########################################################################
#
VerdeAlto = np.array([49, 87, 55])
VerdeBaixo = np.array([49, 87, 55])

# 
########################################################################
# Definindo a Graduação de Verde Presente no Fundo
########################################################################
#
mask = cv.inRange(frame, VerdeBaixo, VerdeAlto)
res = cv.bitwise_and(frame, frame, mask = mask)

f = frame - res
f = np.where(f == 0, image, f)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", f)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()
exit()
########################################################################
# FIM DO PROGRAMA
########################################################################
