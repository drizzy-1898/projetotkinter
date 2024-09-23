import tkinter as tk

class Label_Tkinter():
    def iniciar(self):
        janela = tk.Tk()
        janela.title("Exemplo Label")

        label = tk.Label(janela, text="Apenas um teste")
        label.pack(pady=50)

        janela.mainloop()