import tkinter as tk
import pyautogui

# Função que atualiza a posição do mouse em tempo real
def update_mouse_position():
    x, y = pyautogui.position()
    position_label.config(text=f"Posição do Mouse: X={x}, Y={y}")
    # Agendar a próxima atualização
    root.after(50, update_mouse_position)

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Posição do Mouse em Tempo Real")
root.geometry("300x100")

# Manter a janela sempre no topo
root.attributes("-topmost", True)

# Label para exibir a posição do mouse
position_label = tk.Label(root, text="Posição do Mouse: X=0, Y=0", font=("Arial", 12))
position_label.pack(pady=20)

# Iniciar a atualização da posição do mouse
update_mouse_position()

# Inicia a interface
root.mainloop()