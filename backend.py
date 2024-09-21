import pandas as pd
import os
import re
from datetime import datetime

CLIENTE_FILE = 'clientes.csv'
MANUTENCAO_FILE = 'manutencoes.csv'

def set_diretorio(diretorio):
    global CLIENTE_FILE, MANUTENCAO_FILE
    CLIENTE_FILE = os.path.join(diretorio, 'clientes.csv')
    MANUTENCAO_FILE = os.path.join(diretorio, 'manutencoes.csv')

def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        return pd.read_csv(nome_arquivo)
    else:
        return pd.DataFrame()

def salvar_dados(df, nome_arquivo):
    df.to_csv(nome_arquivo, index=False)

# Outras funções permanecem inalteradas



def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email) is not None

def validar_telefone(telefone):
    padrao_telefone = r'^\+?\d{9,15}$'
    return re.match(padrao_telefone, telefone) is not None

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def cadastrar_cliente(nome, email, telefone):
    df_clientes = carregar_dados(CLIENTE_FILE)
    novo_cliente = pd.DataFrame({
        'Nome': [nome],
        'Email': [email],
        'Telefone': [telefone]
    })
    df_clientes = pd.concat([df_clientes, novo_cliente], ignore_index=True)
    salvar_dados(df_clientes, CLIENTE_FILE)

def cadastrar_manutencao(cliente_nome, descricao, data_entrada, status):
    df_manutencoes = carregar_dados(MANUTENCAO_FILE)
    nova_manutencao = pd.DataFrame({
        'Cliente': [cliente_nome],
        'Descrição': [descricao],
        'Data de Entrada': [data_entrada],
        'Status': [status]
    })
    df_manutencoes = pd.concat([df_manutencoes, nova_manutencao], ignore_index=True)
    salvar_dados(df_manutencoes, MANUTENCAO_FILE)

def atualizar_cliente(nome_cliente, novo_email=None, novo_telefone=None):
    df_clientes = carregar_dados(CLIENTE_FILE)
    if novo_email:
        df_clientes.loc[df_clientes['Nome'] == nome_cliente, 'Email'] = novo_email
    if novo_telefone:
        df_clientes.loc[df_clientes['Nome'] == nome_cliente, 'Telefone'] = novo_telefone
    salvar_dados(df_clientes, CLIENTE_FILE)

def atualizar_manutencao(cliente_nome, nova_descricao=None, nova_data_entrada=None, novo_status=None):
    df_manutencoes = carregar_dados(MANUTENCAO_FILE)
    if nova_descricao:
        df_manutencoes.loc[df_manutencoes['Cliente'] == cliente_nome, 'Descrição'] = nova_descricao
    if nova_data_entrada:
        df_manutencoes.loc[df_manutencoes['Cliente'] == cliente_nome, 'Data de Entrada'] = nova_data_entrada
    if novo_status:
        df_manutencoes.loc[df_manutencoes['Cliente'] == cliente_nome, 'Status'] = novo_status
    salvar_dados(df_manutencoes, MANUTENCAO_FILE)

def excluir_cliente(nome_cliente):
    df_clientes = carregar_dados(CLIENTE_FILE)
    df_clientes = df_clientes[df_clientes['Nome'] != nome_cliente]
    salvar_dados(df_clientes, CLIENTE_FILE)

def excluir_manutencao(cliente_nome):
    df_manutencoes = carregar_dados(MANUTENCAO_FILE)
    df_manutencoes = df_manutencoes[df_manutencoes['Cliente'] != cliente_nome]
    salvar_dados(df_manutencoes, MANUTENCAO_FILE)

def pesquisar_cliente(nome_cliente):
    df_clientes = carregar_dados(CLIENTE_FILE)
    return df_clientes[df_clientes['Nome'] == nome_cliente]

def visualizar_manutencoes():
    return carregar_dados(MANUTENCAO_FILE)
