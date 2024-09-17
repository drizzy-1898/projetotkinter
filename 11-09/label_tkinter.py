import tkinter as tk


janela = tk.Tk()
janela.title("Rxemplo Label")

label = tk.Label(janela, text="Apenas um teste")
label.pack(pady=50)

janela.mainloop()