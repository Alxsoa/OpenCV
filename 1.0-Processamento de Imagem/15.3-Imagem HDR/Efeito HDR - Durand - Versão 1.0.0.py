# Referencia
# https://github.com/spmallick/learnopencv/tree/master/hdr
# https://digital-photography-school.com/getting-real-hdr/
# https://digital-photography-school.com/bracketing-what-is-it-and-what-to-do-with-the-images/
# https://docs.opencv.org/3.4/d2/df0/tutorial_py_hdr.html
# https://www.toptal.com/opencv/python-image-processing-in-computational-photography
# https://github.com/vivianhylee/high-dynamic-range-image
# https://towardsdatascience.com/a-simple-hdr-implementation-on-opencv-python-2325dbd9c650
#

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
def ImagensExposicao ():
  
  Exposicao = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
  NomeArquivos = [
                  "/home/asoares/OpenCV/Imagens/img_0.033.jpg", 
                  "/home/asoares/OpenCV/Imagens/img_0.25.jpg", 
                  "/home/asoares/OpenCV/Imagens/img_2.5.jpg", 
                  "/home/asoares/OpenCV/Imagens/img_15.jpg"
                 ]

  imgImagens = []
  for Nome in NomeArquivos:
      imgTmp = cv.imread(Nome)
      imgImagens.append(imgTmp)
  
  return (imgImagens, Exposicao)

# 
########################################################################
# Leitura das Imagens e Exposições
########################################################################
#
lstImagens, Exposicao = ImagensExposicao()

# 
########################################################################
# Alinhando as Imagens
########################################################################
#
alignMTB = cv.createAlignMTB()
alignMTB.process(lstImagens, lstImagens)

# 
########################################################################
# Obtendo Camera Response Function (CRF)
########################################################################
#
calibrateDebevec = cv.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(lstImagens, Exposicao)

# 
########################################################################
# Juntando as Imgens de Maneira Linear
########################################################################
#
mergeDebevec = cv.createMergeDebevec()
hdrDebevec = mergeDebevec.process(lstImagens, Exposicao, responseDebevec)

# 
########################################################################
# Usando o Método de Durand para Obter Imagens Coloridas de 24 bits
########################################################################
#
tonemapDurand = cv.createTonemap(2.2)
ldrDurand = tonemapDurand.process(hdrDebevec)
ldrDurand = 3 * ldrDurand

# 
########################################################################
# Preparação para Apresentação dos Resultados
########################################################################
#
lstImagens[0] = cv.resize(lstImagens[0], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[0] = cv.copyMakeBorder (
                                      src=lstImagens[0], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[1] = cv.resize(lstImagens[1], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[1] = cv.copyMakeBorder (
                                      src=lstImagens[1], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[2] = cv.resize(lstImagens[2], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[2] = cv.copyMakeBorder (
                                      src=lstImagens[2], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[3] = cv.resize(lstImagens[3], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[3] = cv.copyMakeBorder (
                                      src=lstImagens[3], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

ldrDurand = cv.resize(ldrDurand, (450, 300), interpolation = cv.INTER_AREA)
ldrDurand = cv.copyMakeBorder (
                                src=ldrDurand, 
                                top=5, 
                                bottom=5, 
                                left=5, 
                                right=5, 
                                borderType=cv.BORDER_CONSTANT, 
                                value=(255,255,255)
                             ) 

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
imgResultado = np.hstack ( [lstImagens[0], lstImagens[1], lstImagens [2], lstImagens [3]])
cv.imshow ( "Imagens com Diferentes Exposicoes", imgResultado)
cv.imshow ( "Efeito Final", ldrDurand)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
