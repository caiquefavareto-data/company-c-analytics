import pandas as pd
import os

# Teste 1: O motor funcionou e criou o arquivo?
def test_arquivo_existe():
    # os.path.exists verifica se o arquivo está na pasta
    assert os.path.exists('vendas_ficticias.csv') == True

# Teste 2: O arquivo gerou as 50 linhas que pedimos?
def test_quantidade_linhas():
    # Lê a base de dados
    df = pd.read_csv('vendas_ficticias.csv')
    
    # Verifica se o tamanho (len) do DataFrame é igual a 50
    assert len(df) == 50

# Teste 3: As colunas vitais estão lá?
def test_colunas_corretas():
    df = pd.read_csv('vendas_ficticias.csv')
    colunas_esperadas = ['ID', 'Produto', 'Cidade', 'Valor_CAD']
    
    # Transforma as colunas do arquivo em uma lista e compara
    assert list(df.columns) == colunas_esperadas