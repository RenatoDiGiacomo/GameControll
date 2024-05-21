## Controller ##
# Up
# down
# left
# right
# a = 1key
# s = 2key
# d = pause/menu

import pygetwindow as gw
from PIL import ImageGrab
import cv2
import pydirectinput
import numpy as np
import time

key = [
    'right',
    'right',
    'right',
    'right',
    'right',
    'right',

]

while True:
    time.sleep(.5)
    pydirectinput.press('s')


# def identify_objects(image_path, object_color):
#     # Carrega a imagem
#     img = ImageGrab.grab(image_path)
#     img_np = np.array(img)
    
#     # Converte a imagem para o espaço de cores HSV
#     hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    
#     # Define os limites para a cor do objeto que você deseja identificar
#     lower_bound = np.array(object_color[0])
#     upper_bound = np.array(object_color[1])
    
#     # Cria uma máscara para a cor do objeto
#     mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
#     # Aplica dilatação para expandir a região do objeto
#     kernel = np.ones((5,5),np.uint8)
#     dilation = cv2.dilate(mask,kernel,iterations = 1)
    
#     # Encontra contornos na imagem dilatada
#     contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
#     # Processa cada contorno para identificar o objeto
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:  # Ajuste o valor de acordo com o tamanho esperado do objeto
#             cv2.drawContours(img_np, [cnt], -1, (0,255,0), 2)
    
#     # Mostra a imagem com os contornos desenhados
#     cv2.imshow('Identified Objects', img_np)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Exemplo de uso
# object_color = [[30, 150, 50], [90, 255, 255]]  # Exemplo de limites para verde claro
# identify_objects('screenshot.png.png', object_color)



# def capture_window_screenshot(window_title):
#     # Obtém a janela pelo título
#     window = gw.getWindowsWithTitle(window_title)[0]
    
#     # Obtém as coordenadas da janela
#     x1, y1, x2, y2 = window.left, window.top, window.left + window.width, window.top + window.height
    
#     # Captura a janela especificada
#     screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
#     # Salva a imagem capturada para visualização
#     filename = f"screenshot.png"
#     screenshot.save(filename)
    
#     # Exibe a imagem capturada

# # Título da janela que você quer capturar
# window_title = "Regen v0.97 - Running Alex Kidd in Miracle world"




# # Captura a imagem da janela especificada

# while True:
#     time.sleep(.2)
#     capture_window_screenshot(window_title)
    



