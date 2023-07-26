# Referencia
# https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/
# https://learnopencv.com/introduction-to-mediapipe/
# https://mlhive.com/2022/02/hand-landmarks-detection-using-mediapipe-in-python
# https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/
# https://www.section.io/engineering-education/creating-a-hand-tracking-module/
# https://techtutorialsx.com/2021/04/24/python-mediapipe-finger-roi/
# https://www.geekering.com/categories/computer-vision/marcellacavalcanti/hand-tracking-and-finger-counting-in-python-with-mediapipe/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import mediapipe as mp
import os

# 
########################################################################
# Definições Gerais
########################################################################
# 
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
WebCam = 2
CameraLargura=800
CameraAltura=600

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
CapturaVideo = cv.VideoCapture(WebCam)
if not CapturaVideo.isOpened():
    os.system ("clear")
    print( "A WebCam Não esta Disponível")
    exit ()

# 
########################################################################
# Definindo o Tamanho da Imagem Capturada pela Câmera
########################################################################
#
CapturaVideo.set(cv.CAP_PROP_FRAME_WIDTH, CameraLargura)
CapturaVideo.set(cv.CAP_PROP_FRAME_HEIGHT,CameraAltura)

# 
########################################################################
# Processo de Captura dos Marcadores de Mãos
########################################################################
# 
with mp_hands.Hands (
                        model_complexity=0,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5
                    ) as hands:
  

  while (True):
    Stats, VideoFrame = CapturaVideo.read()
    VideoFrame = cv.flip(VideoFrame, 1)

# 
########################################################################
# Para melhorar o desempenho, marque a imagem como não gravável 
########################################################################
#     
    VideoFrame.flags.writeable = False
    VideoFrame = cv.cvtColor(VideoFrame, cv.COLOR_BGR2RGB)
    Resultado = hands.process(VideoFrame)

# 
########################################################################
# Para melhorar o desempenho, marque a imagem como gravável 
########################################################################
#   
    VideoFrame.flags.writeable = True
    VideoFrame = cv.cvtColor(VideoFrame, cv.COLOR_RGB2BGR)
    ContagemDedos = 0

    if Resultado.multi_hand_landmarks:
      for hand_landmarks in Resultado.multi_hand_landmarks:
        IndiceMao = Resultado.multi_hand_landmarks.index(hand_landmarks)
        EtiquetaMao = Resultado.multi_handedness[IndiceMao].classification[0].label

        handLandmarks = []
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])

# 
########################################################################
# A posição TIP x deve ser maior ou menor que a posição IP x
########################################################################
#   
        if EtiquetaMao == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
           ContagemDedos = ContagemDedos+1
        elif EtiquetaMao == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
             ContagemDedos = ContagemDedos+1

# 
########################################################################
# A posição TIP y deve ser menor que a posição PIP y
########################################################################
# 
        if handLandmarks[8][1] < handLandmarks[6][1]:       
           ContagemDedos = ContagemDedos+1
        if handLandmarks[12][1] < handLandmarks[10][1]:     
           ContagemDedos = ContagemDedos+1
        if handLandmarks[16][1] < handLandmarks[14][1]:    
           ContagemDedos = ContagemDedos+1
        if handLandmarks[20][1] < handLandmarks[18][1]:     
           ContagemDedos = ContagemDedos+1

# 
########################################################################
# Mostra os Marcadores
########################################################################
#
        mp_drawing.draw_landmarks (
                                    VideoFrame,
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_drawing_styles.get_default_hand_landmarks_style(),
                                    mp_drawing_styles.get_default_hand_connections_style()
                                  )

# 
########################################################################
# Escreve o Resultado da Contagem
########################################################################
#
    cv.putText (
                    VideoFrame, 
                    str(ContagemDedos), 
                    (50, 450), 
                    cv.FONT_HERSHEY_SIMPLEX, 
                    3, 
                    (255, 0, 0), 
                    10
                )

# 
########################################################################
# Apresentando a Captura
########################################################################
#
    cv.imshow( "Contagem dos Dedos", VideoFrame)
    if cv.waitKey(5) & 0xFF == 27:
      break

# 
########################################################################
# Fechando o Janelamento e Camera
########################################################################
# 
cv.destroyAllWindows()
cap.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
