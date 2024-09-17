import tkinter as tk

def mostrar_opcao():
    print(f"Opção selecionada: {opcao.get()}")
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
opcao = tk.StringVar(value="Opcão 1")
radio1 = tk.Radiobutton(janela, text="Opção 1",
                        variable=opcao, value="Opção 1",
                        command=mostrar_opcao)

radio1.pack()

radio2 = tk.Radiobutton(janela, text="Opção 2",
                    variable=opcao, value="Opção 2",
                    command=mostrar_opcao)

radio2.pack()

janela.mainloop()
                        