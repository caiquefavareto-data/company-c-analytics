import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- 1. CONFIGURAÇÃO VISUAL (Padrão Corporativo) ---
# Define o tema visual do Seaborn (fundo branco com grades leves)
sns.set_theme(style="whitegrid")

# Define as cores oficiais da análise (usando uma paleta profissional)
paleta_cores = sns.color_palette("viridis", 4)

# --- 2. CARREGAMENTO E PROCESSAMENTO DOS DADOS ---
df = pd.read_csv('vendas_ficticias.csv')

# Agrupa por cidade e soma, exatamente como na análise textual
# Usamos o .reset_index() para que 'Cidade' volte a ser uma coluna fácil de plotar
faturamento = df.groupby('Cidade')['Valor_CAD'].sum().reset_index()

# Ordena do maior para o menor para o gráfico ficar intuitivo
faturamento = faturamento.sort_values(by='Valor_CAD', ascending=False)


# --- 3. CRIAÇÃO DO GRÁFICO (O Canvas) ---
# Define o tamanho da imagem (proporção 10x6 fica ótima em slides e relatórios)
plt.figure(figsize=(10, 6))


# --- 4. DESENHANDO AS BARRAS (Seaborn) ---
# x é a categoria (Cidade), y é o valor financeiro (Valor_CAD)
chart = sns.barplot(
    data=faturamento,
    x='Cidade',
    y='Valor_CAD',
    palette=paleta_cores,
    edgecolor='black' # Adiciona uma borda fina para destaque
)


# --- 5. FORMATAÇÃO EXECUTIVA (Rótulos e Títulos) ---
# Título principal robusto e padronizado em inglês (foco no mercado local)
plt.title('Total Revenue by Canadian City - Company C', fontsize=18, fontweight='bold', pad=20)

# Rótulos dos eixos mais claros
plt.xlabel('City', fontsize=12)
plt.ylabel('Total Revenue (CAD)', fontsize=12)

# MÁGICA FINANCEIRA: Formatar o eixo Y como moeda (C$ 1,234.56)
# Usamos o matplotlib.ticker para isso
formatter = ticker.StrMethodFormatter('C${x:,.2f}')
chart.yaxis.set_major_formatter(formatter)

# Rotacionar um pouco os nomes das cidades para garantir leitura no tablet
plt.xticks(rotation=15)

# Ajuste fino para nada sair cortado na imagem final
plt.tight_layout()


# --- 6. SALVANDO O RESULTADO (O Arquivo de Saída) ---
# Em ambientes de nuvem, é melhor salvar a imagem do que tentar "mostrar" na tela.
# Isso gera um arquivo definitivo para o seu portfólio.
nome_imagem = 'grafico_faturamento_company_c.png'
plt.savefig(nome_imagem, dpi=300) # dpi=300 garante alta resolução para impressão

print(f"\n--- SUCESSO ---")
print(f"O gráfico executivo da Company C foi gerado e salvo como: {nome_imagem}")
print("Verifique a barra lateral esquerda para ver o arquivo de imagem.\n")