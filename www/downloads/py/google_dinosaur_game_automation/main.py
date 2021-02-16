from time import sleep
import pyautogui#752, 482  #fullscreen  #halfscreen start 523 end 467 (Y)
import time
import keyboard
from pyautogui import position
from pyscreeze import pixel


def checkPixels(target):
    '''works only for left half opera gx browser'''
    istrue = False
    for z in range(467, 524):
        if istrue!=True:

            clr = pyautogui.pixel(285, z)
            if clr == target:

                istrue = True
                return True


target = (83,83,83)

try:
    while True:
        color = checkPixels(target)
        # color = pyautogui.pixel(285, 492)
        #print(color==target, color, sep='|')
        if color:
            #print('jump')
            keyboard.press_and_release('space', do_press=True, do_release=True)


except Exception as e:
    print(e)
    sleep(10000)



# while True:
#     x,y = position()
#     print(x,y)