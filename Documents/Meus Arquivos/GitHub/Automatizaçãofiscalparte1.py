import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 0.1  # Pausa entre ações
pyautogui.FAILSAFE = True  # Permite abortar movendo o mouse para canto superior esquerdo

quantidade = int(input("Quantas vezes repetir? "))

pyautogui.moveTo(269, 383)
pyautogui.click()

print("Posicione o cursor no campo de digitação. Iniciando em 5 segundos...")
time.sleep(3)

for i in range(quantidade):
    pyautogui.write('2102')
    pyautogui.press('down')
    print(f"Repetição {i+1}/{quantidade} concluída")

print("Processo concluído!")