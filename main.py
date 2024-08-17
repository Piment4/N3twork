import tkinter as tk
from PIL import Image, ImageTk
import importlib.util
import os

def load_module(module_path):
    """Carrega um módulo a partir de um arquivo especificado."""
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def execute_module_function(module_path, function_name, center_frame):
    """Executa uma função de um módulo carregado."""
    module = load_module(module_path)
    function = getattr(module, function_name)
    function(center_frame)

def sair():
    root.quit()

def adjust_image_opacity(image, opacity):
    """Ajusta a transparência da imagem."""
    image = image.convert("RGBA")
    alpha = image.split()[3]
    alpha = alpha.point(lambda p: p * opacity)  # Ajusta a opacidade
    image.putalpha(alpha)
    return image

def update_background():
    """Atualiza a imagem de fundo para 1/4 da tela."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    background_image = Image.open("logo.png")  # Substitua "logo.png" pelo caminho da sua imagem
    background_image = background_image.resize((screen_width // 4, screen_height // 4), Image.LANCZOS)  # Redimensiona para 1/4 da tela
    background_image = adjust_image_opacity(background_image, 0.3)  # Ajusta a opacidade conforme necessário
    return ImageTk.PhotoImage(background_image)

def clear_center_frame():
    """Limpa o conteúdo do frame central."""
    for widget in center_frame.winfo_children():
        widget.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("N3twork Soluções - Cadastro de Infraestrutura")
root.geometry("800x600")

# Definir o ícone da janela
root.iconphoto(False, tk.PhotoImage(file="icone.png"))

# Atualiza o fundo
background_photo = update_background()

# Label para exibir a imagem de fundo
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame central para exibir conteúdo
center_frame = tk.Frame(root)
center_frame.pack(expand=True, fill='both')

# Criação do menu superior
menu_bar = tk.Menu(root)

# Menu Cadastro
cadastro_menu = tk.Menu(menu_bar, tearoff=0)
cadastro_menu.add_command(label="Cidade de Atendimento", command=lambda: execute_module_function('cadastro/cidade.py', 'cadastrar_cidade', center_frame))
cadastro_menu.add_command(label="Pop/Site", command=lambda: execute_module_function('cadastro/pop.py', 'cadastrar_pop', center_frame))
cadastro_menu.add_command(label="Rack", command=lambda: execute_module_function('cadastro/rack.py', 'cadastrar_rack', center_frame))
cadastro_menu.add_command(label="Equipamento", command=lambda: execute_module_function('cadastro/equipamento.py', 'cadastrar_equipamento', center_frame))
menu_bar.add_cascade(label="Cadastro", menu=cadastro_menu)

# Menu Consulta
consulta_menu = tk.Menu(menu_bar, tearoff=0)
consulta_menu.add_command(label="Cidade de Atendimento", command=lambda: execute_module_function('consulta/cidade.py', 'consultar_cidade', center_frame))
consulta_menu.add_command(label="Pop/Site", command=lambda: execute_module_function('consulta/pop.py', 'consultar_pop', center_frame))
consulta_menu.add_command(label="Rack", command=lambda: execute_module_function('consulta/rack.py', 'consultar_rack', center_frame))
consulta_menu.add_command(label="Equipamento", command=lambda: execute_module_function('consulta/equipamento.py', 'consultar_equipamento', center_frame))
menu_bar.add_cascade(label="Consulta", menu=consulta_menu)

# Menu Sobre
sobre_menu = tk.Menu(menu_bar, tearoff=0)
sobre_menu.add_command(label="Sobre o Sistema", command=lambda: execute_module_function('sobre/sistema.py', 'sobre_sistema', center_frame))
sobre_menu.add_command(label="Licença", command=lambda: execute_module_function('sobre/licenca.py', 'sobre_licenca', center_frame))
menu_bar.add_cascade(label="Sobre", menu=sobre_menu)

# Menu Sair (sem submenu)
menu_bar.add_command(label="Sair", command=sair)

# Configuração do menu na janela principal
root.config(menu=menu_bar)

# Texto na parte inferior
def create_footer_text():
    footer_text = "Desenvolvido por N3twork Soluções Inteligentes"
    footer_label = tk.Label(root, text=footer_text, font=("Arial", 10), anchor="center")
    footer_label.pack(side="bottom", pady=10)  # Ajuste o `pady` para alterar o espaço abaixo do texto

create_footer_text()

# Atualiza a imagem de fundo ao redimensionar a janela
def on_resize(event):
    global background_photo
    background_photo = update_background()
    background_label.config(image=background_photo)

root.bind("<Configure>", on_resize)

# Execução da aplicação
root.mainloop()
