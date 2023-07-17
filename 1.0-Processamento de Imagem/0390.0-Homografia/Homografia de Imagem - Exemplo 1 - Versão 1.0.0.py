# Referencia
# https://learnopencv.com/homography-examples-using-opencv-python-c/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Funções de Apoio
########################################################################
#
def OperadorMouse(event, x, y, flags, data) :    
    if event == cv.EVENT_LBUTTONDOWN :
        cv.circle(data['Imagem'], (x,y),3, (0,0,255), 5, 16);
        cv.imshow("Imagem Base", data['Imagem']);
        if len(data['Pontos']) < 4 :
            data['Pontos'].append([x,y])

    return ()

def CapturaPontosImagem (im):
# 
########################################################################
# Define a Estrutura de Dados
########################################################################
# 
    data = {}
    data['Imagem'] = im.copy()
    data['Pontos'] = []
    
# 
########################################################################
# Define a Função Callback para Qualer Evento do Mouse
########################################################################
#     
    cv.imshow("Imagem Base",im)
    cv.setMouseCallback("Imagem Base", OperadorMouse, data)
    cv.waitKey(0)
    
# 
########################################################################
# Converte o Vetor para Vetor Numpy
########################################################################
#    
    points = np.vstack(data['Pontos']).astype(float)    
    return (points)

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
ImagemPainel = "Corrida.jpg"
ImagemPraca = "TimesSquare.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + ImagemPraca, cv.IMREAD_COLOR)
imgOrigem = cv.imread ( CaminhoImagem + ImagemPainel, cv.IMREAD_COLOR)
imgDestino = cv.resize(imgBase, (0,0), fx=0.25, fy=0.25, interpolation = cv.INTER_AREA)

# 
########################################################################
# Obtendo o Tamanho da Imagem e Construindo o Vetor de Pontos
########################################################################
#
Tamanho = imgOrigem.shape
ptsOrigem = np.array (
                        [
                        [0,0],
                        [Tamanho[1] - 1, 0],
                        [Tamanho[1] - 1, Tamanho[0] -1],
                        [0, Tamanho[0] - 1 ]
                        ],dtype=float
                     )

# 
########################################################################
# Buscando os Pontos da Imagem
########################################################################
#
print ('Clique na Imagem Quatro Pontos e Pressione ENTER')
ptsDestino = CapturaPontosImagem (imgDestino)

# 
########################################################################
# Calcula a Homografia Entre as Imagens
########################################################################
#
h, status = cv.findHomography(ptsOrigem, ptsDestino)

# 
########################################################################
# Executa a Perspectiva
########################################################################
#
imtTemporaria = cv.warpPerspective(imgOrigem, h, (imgDestino.shape[1],imgDestino.shape[0]))

# 
########################################################################
# Apaga da Imagem Destinada a Receber a Perspectiva
########################################################################
#
cv.fillConvexPoly(imgDestino, ptsDestino.astype(int), 0, 16);

# 
########################################################################
# Junta as Imagens Origem e Destino
########################################################################
#
imgDestino = imgDestino + imtTemporaria

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "Imagem Resultado", imgDestino)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
