# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
#from progress.bar import Bar
import matplotlib.pyplot as plt
import os
import platform
import matplotlib

# 
########################################################################
# Definições Gerais
########################################################################
#
ClearCmd = "clear"  # Em Ambiente Windows deve ser usado cls
DirBase = "OpenCV/"
NomeJanela = "Video Base"
NomeImagem = "Pessoa.jpg"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoImagem = CaminhoBase + "Imagens/" 
CorFundo = (204, 255, 255)
CorCirculo = (49, 87, 55)

# 
########################################################################
# Documentação
########################################################################
#
strDoc = "\
########################################################################\n\
# Documentação do Módulo\n\
########################################################################\n\
# \n\
# Objetivo\n\
# --------\n\
# Alterar o fundo de uma imagem por outra imagem.\n\
# \n\
# Referencia\n\
# ----------\n\
# https://github.com/data-coil/7-Days-Of-Computer-Vision-Projects/tree/main/1.%20Realtime%20Background%20Changing\n\
# \n\
# Versão das Bibliotecas Utilizadas\n\
# ---------------------------------\n\
# OpenCV .......: {0} \n\
# Numpy ........: {1} \n\
# Matplotlib ...: {2} \n\
# \n\
# Versão do Ambiente\n\
# ------------------\n\
# Python ........: {3} \n\
# SO ............: {4} \n\
# \n\
########################################################################\n\
"
os.system (ClearCmd) 
print ( strDoc.format (
                        cv.__version__, 
                        np.__version__, 
                        matplotlib.__version__,
                        platform.python_version(), 
                        platform.system()
                       ) )

# 
########################################################################
# Construindo a Imagem Base
########################################################################
#
imgBase = np.full((480, 640, 3), CorFundo, dtype=np.uint8) 

# 
########################################################################
# Desenhando o Círculo na Imagem Base
########################################################################
#
imgCirculo = imgBase.copy()
cv.circle(imgCirculo, (470, 190), 80, CorCirculo, -1)

# 
########################################################################
# Lendo o Background
########################################################################
#
imgBackground = cv.imread(CaminhoImagem + NomeImagem, -1)

# 
########################################################################
# Garante a Igualdade do Tamanho das Imagens
########################################################################
#
imgBackground = cv.resize(imgBackground, (imgCirculo.shape[1], imgCirculo.shape[0]))
imgBackground = cv.cvtColor(imgBackground, cv.COLOR_BGR2RGB)

# 
########################################################################
# Subtraindo a Imagem Círculo da Imagem Base 
########################################################################
#
imgMascara = imgCirculo-imgBase 

# 
########################################################################
# Aplicando a Mścara no Background
########################################################################
#
imgResultado = imgBackground.copy()
imgResultado[imgMascara!=0] = imgCirculo[imgMascara!=0]

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(3,3,1)
plt.imshow ( imgBase )
plt.title ("Imagem Base", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,2)
plt.imshow ( imgCirculo )
plt.title ("Imagem Círculo", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,3)
plt.imshow ( imgBackground )
plt.title ("Imagem Background", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,4)
plt.imshow ( imgMascara )
plt.title ("Máscara", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,5)
plt.imshow ( imgResultado )
plt.title ("Imagem Resultado", fontsize=11, weight='bold' )

plt.subplots_adjust ( left=0.1,
                      bottom=0.1,
                      right=0.9,
                      top=0.9,
                      wspace=0.4,
                      hspace=0.4 )
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################