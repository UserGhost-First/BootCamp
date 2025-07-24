import pyautogui
import time

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# 1. Bloco de repetições iniciais
quantidade = int(input("Quantas vezes repetir? "))

# Clica no ponto onde iniciam as escritas
pyautogui.moveTo(269, 383)
pyautogui.click()

print("Posicione o cursor no campo de digitação. Iniciando em 3 segundos...")
time.sleep(3)

for i in range(quantidade):
    pyautogui.write('1102')
    pyautogui.press('down')
    print(f"Repetição {i+1}/{quantidade} concluída")

    pyautogui.press('enter', presses=2, interval=0.1)

    pyautogui.write('NFC')

print("Primeira fase concluída!\n")


# 2. Bloco de produtos com atalho Alt+W e navegação por ENTER
repeticao_produtos = 1

# Move até o campo de produto e clica
pyautogui.moveTo(163, 584, duration=0.5)
pyautogui.click()
time.sleep(1)

for i in range(repeticao_produtos):
    # Digita o código do produto
    pyautogui.write('1102')
    
    # Aplica com Alt+W
    pyautogui.hotkey('alt', 'w')
    time.sleep(1)
    
    # Confirma alterações
    pyautogui.press('space')
    time.sleep(2)

    # Navega 3 vezes pra próxima "fileira"
    pyautogui.press('enter', presses=3, interval=0.1)
    time.sleep(0.2)
    
    # Digita o próximo valor
    pyautogui.write('221')
    time.sleep(1)

    # Aplica novamente com Alt+W
    pyautogui.hotkey('alt', 'w')
    print(f"Produto {i+1}/{repeticao_produtos} configurado")
    time.sleep(1)

    pyautogui.press('enter')

print("Processo de produtos concluído!")
