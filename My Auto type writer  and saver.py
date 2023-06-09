#for window only
from subprocess import * #import all from subprocess
import pyautogui #pip install pyautogui 
import time 


process =Popen('C:\\Windows\system32/notepad.exe' ) #open notepad automatic
time.sleep(2)
pyautogui.write('''
This Project Is an auto typer for notepad Dev By Manish check out github profile
https://www.github.com/Manishraj94112''', interval=0.01) #Replace by what you want to write
pyautogui.alert('Auto Typer Task Completed') #popup of task complete
a= pyautogui.prompt('Save file as Name') #file name
pyautogui.hotkey('ctrl','s') #save  hotkey
time.sleep(2)
pyautogui.write(a)
pyautogui.write('.txt')
pyautogui.press('enter') #press enter
#process.terminate()
#github.com/Manish00322
