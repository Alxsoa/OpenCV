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
Desenho = False
ModeExecucao  = True 
ix,iy = -1,-1

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Função de Callback para Controle do Mouse
########################################################################
#
def ExecutaTracado(Evento,x,y,flags,param):
    global ix,iy,Desenho,ModeExecucao

    if Evento == cv.EVENT_LBUTTONDOWN:
       Desenho = True
       ix,iy = x,y

    elif Evento == cv.EVENT_MOUSEMOVE:
         if Desenho == True:
            if ModeExecucao == True:
                cv.rectangle(Imagem,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(Imagem,(x,y),5,(0,0,255),-1)

    elif Evento == cv.EVENT_LBUTTONUP:
         Desenho = False
         if ModeExecucao == True:
            cv.rectangle(Imagem,(ix,iy),(x,y),(0,255,0),-1)
         else:
            cv.circle(Imagem,(x,y),5,(0,0,255),-1)

    return ()
# 
########################################################################
# Janelamento e Instancia de Função
########################################################################
#
cv.namedWindow (NomeJanela)
cv.setMouseCallback (NomeJanela, ExecutaTracado)

# 
########################################################################
# Loop de Execução
########################################################################
#
while(1):
    cv.imshow ( NomeJanela, Imagem)
    k = cv.waitKey(1) & 0xFF

    if k == ord('m'):
        ModeExecucao = not ModeExecucao
    elif k == 27:
        break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

