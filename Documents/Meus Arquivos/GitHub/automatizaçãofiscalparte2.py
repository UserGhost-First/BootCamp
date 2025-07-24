import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 0.1  # Pausa entre ações
pyautogui.FAILSAFE = True  # Permite abortar movendo o mouse para canto superior esquerdo

quantidade = int(input("Quantas vezes repetir? "))

pyautogui.moveTo(152, 587)
pyautogui.click()

print("Posicione o cursor no campo de digitação. Iniciando em 3 segundos...")
time.sleep(3)

for i in range(quantidade):
    pyautogui.write('2102')
    pyautogui.press('down')
    print(f"Repetição {i+1}/{quantidade} concluída")

print("Processo concluído!")
print("Iniciando segunda fase em 3 segundos...")
time.sleep(3)

# Pressiona 'enter' 3 vezes antes do loop
pyautogui.press('enter', presses=3, interval=0.1)

for i in range(quantidade):
    pyautogui.write('221')
    pyautogui.press('up')
    print(f"Fase 2 - Repetição {i+1}/{quantidade} concluída")

print("Segunda fase concluída!")
