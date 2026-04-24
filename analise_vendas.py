import pandas as pd

# 1. Carrega os dados que geramos no passo anterior
df = pd.read_csv('vendas_ficticias.csv')

# 2. Faz a matemática: Agrupa os dados por 'Cidade' e soma o 'Valor_CAD'
faturamento_por_cidade = df.groupby('Cidade')['Valor_CAD'].sum()

# 3. Ordena do maior para o menor faturamento
ranking = faturamento_por_cidade.sort_values(ascending=False)

# 4. Imprime o resultado formatado no terminal
print("\n--- RANKING DE VENDAS DA COMPANY C ---")
print(ranking)
print("--------------------------------------\n")