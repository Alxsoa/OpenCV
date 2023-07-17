# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "CarroFord.jpg"
NomeTemplate = "LogoFord.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem ) 

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)
imgTemplate = cv.imread ( CaminhoImagem + NomeTemplate , 0)
Largura, Altura = imgTemplate.shape[::-1]

# 
########################################################################
# Aplicando o Template e Recuperando os Maximos e Minimos da Imagem
########################################################################
#
imgResultado = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgResultado)

# 
########################################################################
# Acrescentando Outros Modificadores
########################################################################
#
imgCCOEFF = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCOEFF)
imgCCORR = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCORR )
imgCCORR_NORMED = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCORR_NORMED)
imgSQDIFF = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_SQDIFF)
imgSQDIFFNORMED = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_SQDIFF_NORMED)

# 
########################################################################
# Recuperando as Coordenadas (Esquerda Superior e Direita Inferior)
########################################################################
#
xEsquerdaSuperior, yEsquerdaSuperior = max_loc
xDireitaInferior, yDireitaInferior = (xEsquerdaSuperior + Largura, yEsquerdaSuperior+ Altura)

# 
########################################################################
# Desenhando a Identificação do Logo na Imagem
########################################################################
#
cv.rectangle ( imgBase, 
                (xEsquerdaSuperior, yEsquerdaSuperior), 
                (xDireitaInferior, yDireitaInferior ), 
                (0, 0, 255), 
                2 )

# 
########################################################################
# Normalizando e Apresentando a Imagem
########################################################################
#
cv.normalize(imgResultado, imgResultado, 0, 1, cv.NORM_MINMAX, -1 )

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,10))

Grafico.add_subplot(3,3,1)
plt.imshow(imgBase)
plt.title("Imagem Identificada", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,2)
plt.imshow(imgResultado, cmap="gray")
plt.title("TM_CCOEFF_NORMED", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,3)
plt.imshow(imgCCOEFF, cmap="gray")
plt.title("TM_CCOEFF", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,4)
plt.imshow(imgCCORR, cmap="gray")
plt.title("TM_CCORR", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,5)
plt.imshow(imgCCORR_NORMED, cmap="gray")
plt.title("TM_CCORR_NORMED", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,6)
plt.imshow(imgSQDIFF, cmap="gray")
plt.title("TM_SQDIFF", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,7)
plt.imshow(imgSQDIFFNORMED, cmap="gray")
plt.title("TM_SQDIFFNORMED", fontsize=11, weight='bold' )

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.1 )
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
