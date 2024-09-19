import tkinter as tk

class Text_Tkinter():
    def iniciar(self):
        janela = tk.Tk()
        janela.title("Exemplo texto")

        texto = tk.Text(janela, height=5, width=40)
        texto.pack(pady=10)

        janela.mainloop()