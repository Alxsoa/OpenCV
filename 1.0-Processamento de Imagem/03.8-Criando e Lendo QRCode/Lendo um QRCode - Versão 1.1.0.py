# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeImagem  = "QRCode.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgQRCode = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgQRCode is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Inicializando o Detector
########################################################################
#
qrCodeDetector = cv.QRCodeDetector()
qrDados, qrBox, _  = qrCodeDetector.detectAndDecode(imgQRCode)

# 
########################################################################
# Detectando e Decodificando o QRCode
########################################################################
#
if qrBox is not None:
    print ( "Dados Decodificados : ", qrDados )
else:
    print ( "Não foi detectado Nenhuma Informação \n")

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", imgQRCode)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
