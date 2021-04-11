# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 00:07:21 2021

@author: Tejas
"""

import pyautogui
import time 

#while True:
#    time.sleep(1)    
#    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#    print(currentMouseX, currentMouseY)

bodyx = 120
bodyy = 355

time.sleep(2)
pyautogui.moveTo(bodyx, bodyy,1) #body

bodyy += 30

time.sleep(2)
pyautogui.moveTo(bodyx, bodyy,1) #Skecthes

bodyy += 30

time.sleep(2)
pyautogui.moveTo(bodyx, bodyy,1) #Construction

bodyy += 30

time.sleep(2)
pyautogui.moveTo(bodyx, bodyy,1) #Components


