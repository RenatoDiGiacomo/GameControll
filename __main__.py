from nes import NES
import pygame
import pydirectinput
import time

pygame.init()

nes_instance = NES("MegaMan.nes",screen_scale=1)

'''
Up, Left, Down, Right: W, A, S, D
Select, Start:  G, H
A, B: P, L
'''

print(nes_instance.run())
# nes_instance.run()

while True:    
    time.sleep(1)
    pydirectinput.press("H")
    pydirectinput.press("P")
    pydirectinput.press("L")
    








    