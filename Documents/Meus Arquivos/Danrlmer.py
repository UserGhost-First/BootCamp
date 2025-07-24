import pyautogui
import time

pyautogui.FAILSAFE = True  # Move o mouse ao canto superior esquerdo para abortar
time.sleep(3)              # Tempo para focar a janela alvo

while True:
    pyautogui.hotkey('ctrl', 'k')
    pyautogui.write('Dammer', interval=0)
    pyautogui.press('enter')
