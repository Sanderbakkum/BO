from microbit import *
import random

while True:
    

    
    if button_a.is_pressed():
        display.scroll('Random Telefoon Nummer')
   
    if button_b.is_pressed():
        display.scroll('316')
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
        display.scroll(random.randint(0,10))
    
    
