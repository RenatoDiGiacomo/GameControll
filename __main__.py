import subprocess
import time
import keyboard

import pygame
import pydirectinput


subprocess.call(['D:\Renato\Estudo\AI\GameControll\Game\Mesen\\Mesen.exe'])


# '''
# Up, Left, Down, Right: W, A, S, D
# Select, Start:  U,I
# A, B: J,L
# Turbo: N,M
# '''

debounce = True

while debounce:
    time.sleep(1)
    print("m")
    pydirectinput.keyDown("m")
    
    if keyboard.is_pressed('q'):
        debounce = False
