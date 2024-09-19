import tkinter as tk

class CheckButton():
    def iniciar(self):
        def verificar():
            if opcao.get():
                print("Selecionado")
            else:
                print("Não selecionado")

        janela = tk.Tk()
        janela.title("Exemplo CheckButton")
        opcao = tk.IntVar()

        check = tk.Checkbutton(janela, text="Escolha a opção",
                            variable=opcao, command=verificar)
        check.pack(pady=10)
        janela.mainloop()