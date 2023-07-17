# Referencia
# https://github.com/x4nth055/pythoncode-tutorials/blob/master/general/generating-reading-qrcode/generate_qrcode.py

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import qrcode
import sys

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeImagem  = "QRCode.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 
qrData = "www.opencv.org"

# 
########################################################################
# Gerando o QRCode
########################################################################
#
imgQRCode = qrcode.make ( qrData )

# 
########################################################################
# Salvando a Imagem do QRCode
########################################################################
#
imgQRCode.save ( CaminhoImagem + NomeImagem )

########################################################################
# FIM DO PROGRAMA
########################################################################
