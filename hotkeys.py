"""
Dota2 Hack script v 1.3

1.Create Hkey for Skymage
2.Create Hkey for Tinker

"""

print("Loading mods...")
#from win32api import GetKeyState 
#from win32con import VK_CAPITAL 

from pywinauto.application import Application
import pyautogui as p
import keyboard
p.FAILSAFE=False
#import db #custom mod made for Dota2 navigation

#Starting the app

"""
app=Application()
app.start(r"C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe")
app.top_window().draw_outline()
window=app.top_window()
window.set_focus()
"""

#===== STARTING OF MAIN ALGO ==================
interval=0.25
#Skymage Skill set

def sky_mage():
    print("Sky_mage hotkeys Activated....")
    while 1:
        if keyboard.is_pressed('v'):

            keyboard.press_and_release('space')
            p.click(interval=0.1)
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('capslock')
            p.click(interval=0.1)
            x,y=p.position()
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('r')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            keyboard.press_and_release('f1')

            keyboard.press_and_release('e')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            ##keyboard.press_and_release('f1')

            keyboard.press_and_release('tab')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('t')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            ##keyboard.press_and_release('f1')

                
            keyboard.press_and_release('c')
            p.click(interval=0.1)
            keyboard.press_and_release('f1')
        else:
            continue

def tinker():
    # cap space tab t e c r
    print("TINKER hotkeys Activated....")
    while 1:
        if keyboard.is_pressed('v'):

            keyboard.press_and_release('capslock')
            p.click(interval=0.1)
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('space')
            p.click(interval=0.1)
            x,y=p.position()
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('tab')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            #keyboard.press_and_release('f1')

            keyboard.press_and_release('t')
            #p.moveTo(x,y)
            

            keyboard.press_and_release('e')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            keyboard.press_and_release('f1')

            keyboard.press_and_release('e')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            keyboard.press_and_release('f1')

            keyboard.press_and_release('e')
            #p.moveTo(x,y)
            p.click(interval=0.1)
            keyboard.press_and_release('f1')

            keyboard.press_and_release('r')

        else:
            continue
print("Select hero\n1.Tinker\n2.Skywrath Mage")
ch=input("Enter choice:")
if ch=="1":tinker()
if ch=="2":sky_mage()
else:
    print('Choose "1" or "2" only Exiting....')
