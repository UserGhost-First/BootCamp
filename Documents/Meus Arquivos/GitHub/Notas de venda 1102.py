import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

time.sleep(3)

pyautogui.moveTo(115, 383, duration=0.5)
pyautogui.click()

# Número fixo de repetições na nota fiscal
repeticoes_nota_fiscal = 1 

# Primeira etapa: nota fiscal
pyautogui.moveTo(269, 383, duration=0.5)
pyautogui.click()

print("Posicione o cursor no campo de digitação. Iniciando em 3 segundos...")
time.sleep(3)

for i in range(repeticoes_nota_fiscal):
    pyautogui.write('1102')
    print(f"Concluído {i + 1} de {repeticoes_nota_fiscal}")

pyautogui.press('enter', presses=2, interval=0.1)

for i in range(repeticoes_nota_fiscal):
    pyautogui.write('NFC')
    print(f"Concluído {i + 1} de {repeticoes_nota_fiscal}")


# Segunda etapa: produtos
quantidade_produtos = int(input("Quantas vezes repetir para os produtos? "))

pyautogui.moveTo(163, 584, duration=0.5)
pyautogui.click()
time.sleep(2)

for i in range(quantidade_produtos):
    pyautogui.write('1102')
    pyautogui.press('down')
    print(f"Produto {i+1}/{quantidade_produtos} inserido")

pyautogui.press('enter', presses=3, interval=0.1)

for i in range(quantidade_produtos):
    pyautogui.write('221')
    pyautogui.press('up')
    print(f"Produto {i+1}/{quantidade_produtos} atualizado")

pyautogui.moveTo(200, 538, duration=0.5)
pyautogui.click()

print("Segunda fase concluída!")
