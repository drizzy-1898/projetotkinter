import tkinter as tk
from tkinter import messagebox

class Login_Tkinter():
    def iniciar(self):
        def login():
            username = entry_username.get()
            password = entry_password.get()
            
            # Aqui você pode adicionar sua lógica de autenticação
            if username == "admin" and password == "1234":
                messagebox.showinfo("Login", "Login bem-sucedido!")
            else:
                messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

        # Criar a janela principal
        janela = tk.Tk()
        janela.title("Tela de Login")

        # Criar labels e entradas
        label_username = tk.Label(janela, text="Nome de Usuário:")
        label_username.pack(pady=5)

        entry_username = tk.Entry(janela)
        entry_username.pack(pady=5)

        label_password = tk.Label(janela, text="Senha:")
        label_password.pack(pady=5)

        entry_password = tk.Entry(janela, show="*")
        entry_password.pack(pady=5)

        # Criar botão de login
        button_login = tk.Button(janela, text="Login", command=login)
        button_login.pack(pady=20)

        # Iniciar o loop principal da interface
        janela.mainloop()
