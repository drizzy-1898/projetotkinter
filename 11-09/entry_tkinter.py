import tkinter as tk

class Entry_Tkinter():
    def iniciar(self):
        janela = tk.Tk()
        janela.title("Exemplo Entry")

        entrada = tk.Entry(janela)
        entrada.pack(pady=10)

        janela.mainloop()
