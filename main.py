import tkinter as tk
from tkinter import messagebox

def cadastrar_cidade():
    messagebox.showinfo("Cadastro", "Cadastrar Cidade de Atendimento!")

def cadastrar_pop():
    messagebox.showinfo("Cadastro", "Cadastrar Pop/Site!")

def cadastrar_rack():
    messagebox.showinfo("Cadastro", "Cadastrar Rack!")

def cadastrar_equipamento():
    messagebox.showinfo("Cadastro", "Cadastrar Equipamento!")

def consultar_cidade():
    messagebox.showinfo("Consulta", "Consultar Cidade de Atendimento!")

def consultar_pop():
    messagebox.showinfo("Consulta", "Consultar Pop/Site!")

def consultar_rack():
    messagebox.showinfo("Consulta", "Consultar Rack!")

def consultar_equipamento():
    messagebox.showinfo("Consulta", "Consultar Equipamento!")

def sobre_sistema():
    messagebox.showinfo("Sobre", "Sobre o Sistema!")

def sobre_licenca():
    messagebox.showinfo("Sobre", "Informações de Licença!")

def sair():
    root.quit()

# Criação da janela principal
root = tk.Tk()
root.title("N3twork Soluções - Cadastro de Infraestrutura TESTE")
root.geometry("800x600")

# Criação do menu superior
menu_bar = tk.Menu(root)

# Menu Cadastro
cadastro_menu = tk.Menu(menu_bar, tearoff=0)
cadastro_menu.add_command(label="Cidade de Atendimento", command=cadastrar_cidade)
cadastro_menu.add_command(label="Pop/Site", command=cadastrar_pop)
cadastro_menu.add_command(label="Rack", command=cadastrar_rack)
cadastro_menu.add_command(label="Equipamento", command=cadastrar_equipamento)
menu_bar.add_cascade(label="Cadastro", menu=cadastro_menu)

# Menu Consulta
consulta_menu = tk.Menu(menu_bar, tearoff=0)
consulta_menu.add_command(label="Cidade de Atendimento", command=consultar_cidade)
consulta_menu.add_command(label="Pop/Site", command=consultar_pop)
consulta_menu.add_command(label="Rack", command=consultar_rack)
consulta_menu.add_command(label="Equipamento", command=consultar_equipamento)
menu_bar.add_cascade(label="Consulta", menu=consulta_menu)

# Menu Sobre
sobre_menu = tk.Menu(menu_bar, tearoff=0)
sobre_menu.add_command(label="Sobre o Sistema", command=sobre_sistema)
sobre_menu.add_command(label="Licença", command=sobre_licenca)
menu_bar.add_cascade(label="Sobre", menu=sobre_menu)

# Menu Sair
sair_menu = tk.Menu(menu_bar, tearoff=0)
sair_menu.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Sair", menu=sair_menu)

# Configuração do menu na janela principal
root.config(menu=menu_bar)

# Execução da aplicação
root.mainloop()
