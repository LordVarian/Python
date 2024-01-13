import pyautogui, os

os.chdir(r'C:\Users\David Huang\Downloads\Python')

pyautogui.screenshot('screenshot.png')
# pyautogui.locateOnScreen('screenshot.png')
# pyautogui.locateCenterOnScreen('screenshot.png')
pyautogui.moveTo(100, 100)
pyautogui.click()