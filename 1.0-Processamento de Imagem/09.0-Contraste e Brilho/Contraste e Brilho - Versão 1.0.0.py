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
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def Controlador (tmpImagem, Brilho=255, Contraste=127):
    
    Brilho = int((Brilho - 0) * (255 - (-255)) / (510 - 0) + (-255))
    Contraste = int((Contraste - 0) * (127 - (-127)) / (254 - 0) + (-127))
  
    if Brilho != 0:
        if Brilho > 0:
            Sombra = Brilho
            Maximo = 255
        else:
            Sombra = 0
            Maximo = 255 + Brilho
  
        al_pha = (Maximo - Sombra) / 255
        ga_mma = Sombra
        ImagemResultado = cv.addWeighted(tmpImagem, al_pha, tmpImagem, 0, ga_mma)
  
    else:
        ImagemResultado = tmpImagem
  
    if Contraste != 0:
        Alpha = float(131 * (Contraste + 127)) / (127 * (131 - Contraste))
        Gamma = 127 * (1 - Alpha)
        ImagemResultado = cv.addWeighted(ImagemResultado, Alpha, ImagemResultado, 0, Gamma)
  
    return ImagemResultado

def EfeitoContrasteBrilho (Brilho=0):
    Brilho = cv.getTrackbarPos("Brilho", "Processamento de Imagem")
    Contraste = cv.getTrackbarPos("Contraste", "Processamento de Imagem")
    EfeitoResultado = Controlador (Imagem, Brilho, Contraste)
    cv.imshow("Efeito Resultante", EfeitoResultado)
    return ()

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

cv.namedWindow("Processamento de Imagem")
cv.imshow("Processamento de Imagem", Imagem)

cv.createTrackbar("Brilho", "Processamento de Imagem", 255, 2 * 255, EfeitoContrasteBrilho) 
cv.createTrackbar("Contraste", "Processamento de Imagem", 127, 2 * 127, EfeitoContrasteBrilho)  
    
EfeitoContrasteBrilho (0)
cv.waitKey(0)

########################################################################
# FIM DO PROGRAMA
########################################################################
