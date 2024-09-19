import tkinter as tk

class Button_Tkinter():
    def iniciar(self):
        janela = tk.Tk()
        janela.title("Exemplo Button")
        janela.geometry("400x400")

        def on_click_button():
            print("Clicked")

        botao = tk.Button(janela, text="Click Button", command=on_click_button)
        botao.pack(pady=10)





        janela.mainloop()