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
NomeJanela = "Imagem Misturada"
NomeFundo = "Oceano.jpg"
NomeFrente  = "Peixes.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemFundo = cv.imread ( CaminhoImagem + NomeFundo, cv.IMREAD_COLOR)

# 
########################################################################
# Lendo a Imagem Fundo
########################################################################
#
ImagemFrente = cv.imread ( CaminhoImagem + NomeFrente, cv.IMREAD_COLOR)

# 
########################################################################
# Checa se Tem o Mesmo Tamanho
########################################################################
#
AlturaFrente, LarguraFrente, CanaisFrente = ImagemFrente.shape
AlturaFundo, LarguraFundo, CanaisFundo = ImagemFundo.shape

if ( (AlturaFrente==AlturaFundo) & (LarguraFrente==LarguraFundo) & (CanaisFrente==CanaisFundo)):
    print ( "########################################################################" )
    print ( "# Imagens Atendem aos Requisitos ")
    print ( "########################################################################" )    
else:
    print ( "########################################################################" )
    print ( "# Imagens NÃO Atendem aos Requisitos ")
    print ( "########################################################################" )    
    exit ()

# 
########################################################################
# Misturando a Imagem
########################################################################
#
ImagemMisturada = cv.addWeighted(ImagemFrente,0.7,ImagemFundo,0.3,0)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", ImagemMisturada)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
