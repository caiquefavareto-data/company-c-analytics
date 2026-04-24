import pandas as pd
import random

# Função para criar dados fictícios de vendas
def criar_base_ficticia():
    # Listas de mentirinha
    produtos = ['Sensor Alpha', 'Cabo Tipo B', 'Placa de Controle', 'Motor X1']
    cidades = ['Vaughan', 'Toronto', 'Mississauga', 'Brampton']
    
    dados = []
    
    # Criando 50 linhas de dados aleatórios
    for i in range(50):
        venda = {
            'ID': i + 100,
            'Produto': random.choice(produtos),
            'Cidade': random.choice(cidades),
            'Valor_CAD': round(random.uniform(50, 500), 2) # Valores em Dólar Canadense
        }
        dados.append(venda)
    
    # Transformando em uma tabela (DataFrame)
    df = pd.DataFrame(dados)
    
    # Salvando em CSV
    df.to_csv('vendas_ficticias.csv', index=False)
    print("Arquivo 'vendas_ficticias.csv' criado com sucesso!")

# Executando a função
if __name__ == "__main__":
    criar_base_ficticia()