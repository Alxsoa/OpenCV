# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Construindo a Matriz 
########################################################################
#
CorPreta = (0, 0, 0)
imgRetangulo = np.full((300, 300, 3), CorPreta, dtype=np.uint8) 
imgCirculo = np.full((300, 300, 3 ), CorPreta, dtype=np.uint8) 

# 
########################################################################
# Desenhando as Figuras nas Imagens
########################################################################
#
imgRetangulo = cv.rectangle (imgRetangulo, (25, 25), (275, 275), (255,255,255), -1)
imgCirculo = cv.circle (imgCirculo, (150, 150), 150, (255,255,255), -1)

# 
########################################################################
# Executando a Operação AND Entre as Imagens
########################################################################
#
bitwiseAnd = cv.bitwise_and(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação OR Entre as Imagens
########################################################################
#
bitwiseOr = cv.bitwise_or(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação XOR Entre as Imagens
########################################################################
#
bitwiseXor = cv.bitwise_xor(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação NOT na Imagem Círculo
########################################################################
#
bitwiseNotCirculo = cv.bitwise_not (imgCirculo)

# 
########################################################################
# Executando a Operação NOT na Imagem Retangulo
########################################################################
#
bitwiseNotRetangulo = cv.bitwise_not (imgRetangulo)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
cv.imshow ("Retangulo",imgRetangulo)
cv.imshow ("Circulo",imgCirculo)
cv.imshow ("Bitwise AND", bitwiseAnd)
cv.imshow ("Bitwise OR", bitwiseOr)
cv.imshow ("Bitwise XOR", bitwiseXor)
cv.imshow ("Bitwise NOT Circulo", bitwiseNotCirculo)
cv.imshow ("Bitwise NOT Retangulo", bitwiseNotRetangulo)

cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################