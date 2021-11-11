#for window only
from subprocess import * #import all from subprocess
import pyautogui #pip install pyautogui 
import time 

writer = input("Write your Note : ")
process =Popen('C:\\Windows\system32/notepad.exe' ) #open notepad automatic
time.sleep(2)
pyautogui.write(writer, interval=0.01) #input from writer
pyautogui.alert('Auto Typer Task Completed') #popup of task complete
a= pyautogui.prompt('Save file as Name') #file name
pyautogui.hotkey('ctrl','s') #save  hotkey
time.sleep(2) #after 2 sec
pyautogui.write(a)
pyautogui.write('.txt')
pyautogui.press('enter') #press enter
#process.terminate()
#github.com/Manishraj94112
