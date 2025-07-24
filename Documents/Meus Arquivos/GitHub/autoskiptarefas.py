import pyautogui
import time

# Defina as variáveis que você quer personalizar
x = 1747   # posição X
y = 541   # posição Y
intervalo = 2  # tempo entre os cliques em segundos
vezes = 1000000000000

for i in range(vezes):
    pyautogui.click(x, y)
    print(f"Clique {i+1} em ({x},{y})")
    time.sleep(intervalo)

print("Finalizado!")