# Referencia
# https://docs.opencv.org/4.x/d3/d50/group__imgproc__colormap.html

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def NomeMapaCor (id) :
    switcher = {
                    0 : "COLORMAP_AUTUMN",
                    1 : "COLORMAP_BONE",
                    2 : "COLORMAP_JET",
                    3 : "COLORMAP_WINTER",
                    4 : "COLORMAP_RAINBOW",
                    5 : "COLORMAP_OCEAN",
                    6 : "COLORMAP_SUMMER",
                    7 : "COLORMAP_SPRING",
                    8 : "COLORMAP_COOL",
                    9 : "COLORMAP_HSV",
                    10: "COLORMAP_PINK",
                    11: "COLORMAP_HOT",
                    12: "COLORMAP_PARULA",
                    13: "COLORMAP_MAGMA",
                    14: "COLORMAP_INFERNO",
                    15: "COLORMAP_PLASMA",
                    16: "COLORMAP_VIRIDIS",
                    17: "COLORMAP_CIVIDIS",
                    18: "COLORMAP_TWILIGHT",
                    19: "COLORMAP_TWILIGHT_SHIFTED",
                    20: "COLORMAP_TURBO",
                    21: "COLORMAP_DEEPGREEN"
                }
    return switcher.get(id, "NONE")

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "OpenCV/"
NomeJanela = "Imagem Reduzida"
NomeImagem  = "Monalisa.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
imgReduzida = cv.resize(imgBase, (250, 350), interpolation = cv.INTER_AREA)
imgTemporaria = np.zeros((250, 350, 3), np.uint8);

iLinha = 1
Grafico = plt.figure(figsize=(12, 15))
for iAux in range (0,21):
    imgTemporaria = cv.applyColorMap(imgReduzida, iAux)
    imgTemporaria = cv.cvtColor(imgTemporaria, cv.COLOR_BGR2RGB)

    Grafico.add_subplot(1,4,iLinha)
    plt.imshow ( imgTemporaria )
    plt.title ( NomeMapaCor (iAux) , fontsize=9 )

    if ( iLinha == 4 ):
        plt.show ()
        Grafico = plt.figure(figsize=(12, 15))
        iLinha = 1
    else:
        iLinha = iLinha + 1

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
