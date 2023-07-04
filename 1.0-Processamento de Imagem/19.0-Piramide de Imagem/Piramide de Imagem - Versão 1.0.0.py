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
NomeJanela = "Pirâmide de Imagem"
NomeImagem  = "Olho.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
imgReduzida = cv.resize(Imagem, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)

while True:
    nLinhas, nColunas, _channels = map(int, imgReduzida.shape)  
    cv.imshow ( "JanelaBase", imgReduzida)
    cv.setWindowTitle("JanelaBase", NomeJanela )    
    Tecla = cv.waitKey(0)
    if Tecla == 27:
        break
        
    elif chr(Tecla) == 'i':
        imgReduzida = cv.pyrUp(imgReduzida, dstsize=(2 * nColunas, 2 * nLinhas))
        
    elif chr(Tecla) == 'o':
        imgReduzida = cv.pyrDown(imgReduzida, dstsize=(nColunas // 2, nLinhas // 2))

# 
########################################################################
# Destrói o Janelamento
########################################################################
#        
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
