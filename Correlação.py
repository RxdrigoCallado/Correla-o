import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import numpy as np

def obter_dados_ativos(num_dias, todos_ativos, nome_arquivo):
    data_inicio = datetime.now() - timedelta(days=num_dias)
    data_fim = datetime.now()
    df_final = pd.DataFrame()
    
    for ativos_nome, ativos in todos_ativos.items():
        precos = obter_precos_ativos(ativos, data_inicio, data_fim)
        precos = tratar_valores_nulos(precos)
        df_final = pd.concat([df_final, precos], axis=1)
    
    df_final = tratar_valores_nulos(df_final)  # Tratamento adicional após a concatenação
    salvar_dados(df_final, nome_arquivo, data_inicio, data_fim, todos_ativos)

def obter_precos_ativos(tickers, data_inicio, data_fim):
    dados = yf.download(tickers, start=data_inicio, end=data_fim, interval='1d')['Close']
    return dados

def tratar_valores_nulos(df):
    for coluna in df.columns:
        # Substituir zeros por NaN
        df[coluna] = df[coluna].replace(0, np.nan)
        
        # Preencher valores nulos com o valor não-nulo mais próximo
        df[coluna] = df[coluna].fillna(method='ffill').fillna(method='bfill')
        
        # Se ainda houver valores nulos (caso toda a coluna seja nula), substituir por 0
        df[coluna] = df[coluna].fillna(0)
        
        # Converter possíveis strings vazias para NaN e então para 0
        df[coluna] = df[coluna].replace('', np.nan).fillna(0)
    
    return df

def salvar_dados(dados, nome_arquivo, data_inicio, data_fim, todos_ativos):
    dados.index = pd.to_datetime(dados.index)
    dados['Data de Referencia'] = dados.index.strftime('%d/%m/%Y')
    dados.reset_index(drop=True, inplace=True)
    
    # Verificação final para garantir que não haja valores nulos
    dados = dados.fillna(0)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], initialfile=nome_arquivo)
    if file_path:
        modo = 'a' if os.path.exists(file_path) else 'w'
        with pd.ExcelWriter(file_path, engine='openpyxl', mode=modo) as writer:
            dados.to_excel(writer, sheet_name='Dados', index=False)
            calcular_variacao(dados, todos_ativos, writer)
        messagebox.showinfo("Sucesso", f"Dados salvos em {file_path}")

def calcular_variacao(dados, todos_ativos, writer):
    variacoes = {}
    
    for ativo_grupo, tickers in todos_ativos.items():
        if len(tickers) == 2:
            ativo, commodity = tickers

            # Cálculo da variação para cada ativo
            variacao_ativo = (dados[ativo].iloc[-1] / dados[ativo].iloc[0]) - 1
            variacao_commodity = (dados[commodity].iloc[-1] / dados[commodity].iloc[0]) - 1
            
            variacoes[f'Variação {ativo}'] = variacao_ativo
            variacoes[f'Variação {commodity}'] = variacao_commodity

            # Cálculo da variação do ativo em relação à commodity
            if variacao_commodity != 0:
                variacao_relativa = variacao_ativo / variacao_commodity
                variacoes[f'Variação Relativa {ativo} / {commodity}'] = variacao_relativa

    df_variacoes = pd.DataFrame(variacoes, index=[0])

    # Salvar em planilha Excel
    df_variacoes.to_excel(writer, sheet_name='Variações', index=False)

def criar_interface_grafica(todos_ativos, nome_arquivo):
    window = tk.Tk()
    window.title("Obter Dados de Ativos")
    window.geometry("300x200")

    label_explicativo = tk.Label(window, text="Insira o número de dias para obter os dados:")
    label_explicativo.pack(pady=10)

    entry_dias = tk.Entry(window)
    entry_dias.pack(pady=5)

    button_obter_dados = tk.Button(window, text="Obter Dados", command=lambda: obter_dados_ativos(int(entry_dias.get()), todos_ativos, nome_arquivo))
    button_obter_dados.pack(pady=20)

    window.mainloop()

# Lista de ativos - Vale, PRIO e AURA
todos_ativos = {
    "VALE": ['VALE3.SA', 'TIO=F'],
    "PRIO": ['PRIO3.SA', 'BZ=F'],
    "AURA": ['AURA33.SA', 'GC=F'],
    "TSM": ['TSM', '^SOX']
}
nome_arquivo = "Ativos"

# Criar interface gráfica para Vale, PRIO e AURA
criar_interface_grafica(todos_ativos, nome_arquivo)