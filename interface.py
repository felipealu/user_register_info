import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import backend 

def escolher_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        backend.set_diretorio(diretorio)
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
        messagebox.showinfo("Sucesso", f"Diretório alterado para:\n{diretorio}")

def cadastrar_cliente():
    nome = simpledialog.askstring("Cadastro de Cliente", "Nome do Cliente:")
    
    email = simpledialog.askstring("Cadastro de Cliente", "Email do Cliente:")
    simpledialog.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    telefone = simpledialog.askstring("Cadastro de Cliente", "Telefone do Cliente:")
    simpledialog.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    
    if not backend.validar_email(email):
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico") 
        messagebox.showerror("Erro", "Email inválido!")
        return
    if not backend.validar_telefone(telefone):
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico") 
        messagebox.showerror("Erro", "Telefone inválido!")
        return
    
    backend.cadastrar_cliente(nome, email, telefone)
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico") 
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

def cadastrar_manutencao():
    cliente_nome = simpledialog.askstring("Cadastro de Manutenção", "Nome do Cliente:")
    descricao = simpledialog.askstring("Cadastro de Manutenção", "Descrição do Problema:")
    data_entrada = simpledialog.askstring("Cadastro de Manutenção", "Data de Entrada (dd/mm/aaaa):")
    status = simpledialog.askstring("Cadastro de Manutenção", "Status (Aberto/Fechado):")
    
    if not backend.validar_data(data_entrada):
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
        messagebox.showerror("Erro", "Data inválida!")
        return
    
    backend.cadastrar_manutencao(cliente_nome, descricao, data_entrada, status)
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    messagebox.showinfo("Sucesso", "Manutenção cadastrada com sucesso!")

def atualizar_cliente():
    nome_cliente = simpledialog.askstring("Atualizar Cliente", "Informe o nome do cliente a ser atualizado:")
    novo_email = simpledialog.askstring("Atualizar Cliente", "Novo Email (deixe em branco para manter):")
    novo_telefone = simpledialog.askstring("Atualizar Cliente", "Novo Telefone (deixe em branco para manter):")
    
    backend.atualizar_cliente(nome_cliente, novo_email, novo_telefone)
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

def atualizar_manutencao():
    cliente_nome = simpledialog.askstring("Atualizar Manutenção", "Informe o nome do cliente com a manutenção a ser atualizada:")
    nova_descricao = simpledialog.askstring("Atualizar Manutenção", "Nova Descrição (deixe em branco para manter):")
    nova_data_entrada = simpledialog.askstring("Atualizar Manutenção", "Nova Data de Entrada (deixe em branco para manter):")
    novo_status = simpledialog.askstring("Atualizar Manutenção", "Novo Status (deixe em branco para manter):")
    
    backend.atualizar_manutencao(cliente_nome, nova_descricao, nova_data_entrada, novo_status)
    messagebox.showinfo("Sucesso", "Manutenção atualizada com sucesso!")
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")


def excluir_cliente():
    nome_cliente = simpledialog.askstring("Excluir Cliente", "Informe o nome do cliente a ser excluído:")
    backend.excluir_cliente(nome_cliente)
    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico") 
def excluir_manutencao():
    cliente_nome = simpledialog.askstring("Excluir Manutenção", "Informe o nome do cliente com a manutenção a ser excluída:")
    backend.excluir_manutencao(cliente_nome)
    messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    messagebox.showinfo("Sucesso", "Manutenção excluída com sucesso!")

def pesquisar_cliente():
    nome_cliente = simpledialog.askstring("Pesquisar Cliente", "Informe o nome do cliente:")
    cliente_info = backend.pesquisar_cliente(nome_cliente)
    
    if not cliente_info.empty:
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
        messagebox.showinfo("Cliente Encontrado", cliente_info.to_string(index=False))
    else:
        messagebox.showerror("Erro", "Cliente não encontrado!")
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico") 

def visualizar_manutencoes():
    manutencoes = backend.visualizar_manutencoes()
    if manutencoes.empty:
        messagebox.showinfo("Visualizar Manutenções", "Nenhuma manutenção cadastrada.")
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")
    
    else:
        messagebox.showinfo("Visualizar Manutenções", manutencoes.to_string())
        messagebox.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")

def criar_interface():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro da Aviva Info")
    janela.geometry("800x600")
    janela.iconbitmap("C:/Users/felip/Desktop/Faculdade/banco de icones/menu_info.ico")  
    

    style = ttk.Style()
    style.theme_use("alt")
    style.configure("TButton", background="#ffeb3b", foreground="#000000", font=("Goudy Old Style", 17), borderwidth=8)
    style.map("TButton", background=[("active", "#ffc107")])
    style.configure("TNotebook.Tab", background="#ffeb3b", padding=[10, 5])
    style.map("TNotebook.Tab", background=[("selected", "#ffc107")])
    
    menu_bar = tk.Menu(janela)
    menu_arquivo = tk.Menu(menu_bar, tearoff=0)
    menu_arquivo.add_command(label="Escolher Diretório", command=escolher_diretorio)
    menu_arquivo.add_command(label="Sair", command=janela.quit)
    menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

    tab_control = ttk.Notebook(janela)
    tab_cliente = ttk.Frame(tab_control)
    tab_manutencao = ttk.Frame(tab_control)
    tab_visualizar = ttk.Frame(tab_control)

    tab_control.add(tab_cliente, text="Clientes")
    tab_control.add(tab_manutencao, text="Manutenções")
    tab_control.add(tab_visualizar, text="Visualizar")

    btn_cadastrar_cliente = ttk.Button(tab_cliente, text="Cadastrar Cliente", command=cadastrar_cliente)
    btn_atualizar_cliente = ttk.Button(tab_cliente, text="Atualizar Cliente", command=atualizar_cliente)
    btn_excluir_cliente = ttk.Button(tab_cliente, text="Excluir Cliente", command=excluir_cliente)
    btn_pesquisar_cliente = ttk.Button(tab_cliente, text="Pesquisar Cliente", command=pesquisar_cliente)

    btn_cadastrar_cliente.pack(pady=10, padx=10, fill='x', expand=True)
    btn_atualizar_cliente.pack(pady=10, padx=10, fill='x', expand=True)
    btn_excluir_cliente.pack(pady=10, padx=10, fill='x', expand=True)
    btn_pesquisar_cliente.pack(pady=10, padx=10, fill='x', expand=True)

    btn_cadastrar_manutencao = ttk.Button(tab_manutencao, text="Cadastrar Manutenção", command=cadastrar_manutencao)
    btn_atualizar_manutencao = ttk.Button(tab_manutencao, text="Atualizar Manutenção", command=atualizar_manutencao)
    btn_excluir_manutencao = ttk.Button(tab_manutencao, text="Excluir Manutenção", command=excluir_manutencao)

    btn_cadastrar_manutencao.pack(pady=10, padx=10, fill='x', expand=True)
    btn_atualizar_manutencao.pack(pady=10, padx=10, fill='x', expand=True)
    btn_excluir_manutencao.pack(pady=10, padx=10, fill='x', expand=True)

    btn_visualizar_manutencoes = ttk.Button(tab_visualizar, text="Visualizar Manutenções", command=visualizar_manutencoes)

    btn_visualizar_manutencoes.pack(pady=10, padx=10, fill='x', expand=True)

    tab_control.pack(expand=1, fill="both")
    janela.config(menu=menu_bar)
    
    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
