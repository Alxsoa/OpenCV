# Referencia
# https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "LinhasEstacionamento2.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem ) 

# 
########################################################################
# Reduzindo o tamanh da Imagem
########################################################################
#
imgBase = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor ( imgBase, cv.COLOR_BGR2GRAY )

# 
########################################################################
# Reduzindo o Ruído
########################################################################
#
TamanhoKernel = 5
imgSemRuido = cv.GaussianBlur(imgCinza,(TamanhoKernel, TamanhoKernel),0)

# 
########################################################################
# Destacando Contornos
########################################################################
#
LimiteBaixo = 50
LimiteAlto  = 150
imgContornos = cv.Canny(imgSemRuido, LimiteBaixo, LimiteAlto)

# 
########################################################################
# Parametros da Busca de Linhas
########################################################################
#
Rho = 1 # resolução de distância em pixels da grade Hough
Theta = np.pi / 180 # resolução angular em radianos da grade Hough
Threshold = 15 # número mínimo de votos (interseções na célula da grade Hough)
MinLineLength = 50 # número mínimo de pixels que compõem uma linha
MaxLineGap = 20 # intervalo máximo em pixels entre segmentos de linha conectáveis
line_image = np.copy(imgBase) * 0 # criando um espaço em branco para desenhar linhas

# 
########################################################################
# Buscando as Linhas
########################################################################
#
lines = cv.HoughLinesP (
                            imgContornos, 
                            Rho, 
                            Theta, 
                            Threshold, 
                            np.array([]),
                            MinLineLength, 
                            MaxLineGap
                        )

# 
########################################################################
# Construindo as Linhas
########################################################################
#
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

# 
########################################################################
# Desenhando as Linhas
########################################################################
#
lines_edges = cv.addWeighted ( 
                                imgBase, 
                                0.8, 
                                line_image, 
                                1, 
                                0
                             )

# 
########################################################################
# Apresentando os Resultados
########################################################################
#
cv.imshow("Resultado",lines_edges)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
