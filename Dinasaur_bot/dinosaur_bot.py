from PIL import ImageGrab, ImageOps
import time
import pyautogui
from numpy import *

class Coordinates():
    replayBtn = (396,387)
    dinasaur = (178,394)
    
def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)    
    print("jump")
    pyautogui.keyUp('space')
    
def imageGrab():
    box = (Coordinates.dinasaur[0]+60,Coordinates.dinasaur[1],Coordinates.dinasaur[0]+100,Coordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())         
    return(a.sum())
       
         
def main():         
    restartGame()
    while True:                    
        if(imageGrab!=1447):   
            pressSpace()        
            time.sleep(0.1)
                                     
            
main()
