import pyautogui
import random
import string
import time

time.sleep(3)

def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Loop para realizar a ação 20 vezes
for _ in range(5):
    # Pressione CTRL+L
    pyautogui.hotkey('ctrl', 'k')
    
    # Espere um curto período de tempo para que a caixa de diálogo apareça (ajuste conforme necessário)
    time.sleep(0)
    
    # Gere uma palavra aleatória com 8 caracteres
    word = random_word(7)

    
    # Insira a palavra gerada
    pyautogui.typewrite(word)
    
    # Pressione Enter
    pyautogui.press('enter')
    
    # Espere um pouco antes da próxima iteração (ajuste conforme necessário)
    time.sleep(6)