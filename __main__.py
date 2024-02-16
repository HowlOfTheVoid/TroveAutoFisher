'''
Created on Jun 19, 2023

@author: ender
'''

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

def main():
    print("Alright, master! I'm ready to help you with fishing.")
    print("Just point the cursor somewhere you want to fish, and that")
    print("Your Lures are set to the 'T' key!")
    
    numLures = input("How many lures do you have?")
    
    input("Waiting for Enter...")
    
    
    keyboard = KeyboardController()
    mouse = MouseController()
    
    mouse.click(Button.left, 1)
    
    for x in range(int(numLures)):
        keyboard.press('t')
        keyboard.release('t')
        for y in range(130):
            keyboard.press('f')
            time.sleep(0.25)
            keyboard.release('f')
            time.sleep(13.4)
            keyboard.press('f')
            time.sleep(0.25)
            keyboard.release('f')
            time.sleep(13.4)
            
    print("Alright! Done!")
    
    
if __name__ == "__main__":
    main()