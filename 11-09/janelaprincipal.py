import tkinter as tk

class Janela_Principal():
    def exibir_janela(self):
        janela = tk.Tk()
        janela.title("Janela Principal")
        janela.geometry("200x200")

        janela.mainloop()