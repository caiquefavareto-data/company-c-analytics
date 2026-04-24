import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- 1. CONFIGURAÇÃO VISUAL AVANÇADA (O Toque de Mestre) ---
# Define o tema visual do Seaborn (fundo branco limpo, sem grades)
sns.set_theme(style="white")

# Define as cores oficiais customizadas da Company C
# Azul Marinho para Destaque, Dourado Nobre para os outros
cor_destaque = "#001F3F" # Navy Blue
cor_padrao = "#DAA520"   # Goldenrod
# Usamos a lógica 'Se a cidade for Vaughan, use destaque, senão, cor padrão'
# (Isso é feito diretamente na plotagem abaixo)


# --- 2. CARREGAMENTO E PROCESSAMENTO DOS DADOS ---
# (Essa parte continua igual, é o nosso motor de dados)
df = pd.read_csv('vendas_ficticias.csv')
faturamento = df.groupby('Cidade')['Valor_CAD'].sum().reset_index()
faturamento = faturamento.sort_values(by='Valor_CAD', ascending=False)


# --- 3. CRIAÇÃO DO GRÁFICO (Canvas e Design) ---
# Define o tamanho da imagem (proporção 10x6)
plt.figure(figsize=(10, 6))

# Define a paleta de cores customizada com base nos dados reais
# Criamos uma lista de cores que corresponde à ordem das cidades no DataFrame
paleta_customizada = [cor_destaque if cidade == 'Vaughan' else cor_padrao for cidade in faturamento['Cidade']]


# --- 4. DESENHANDO AS BARRAS (Seaborn) ---
chart = sns.barplot(
    data=faturamento,
    x='Cidade',
    y='Valor_CAD',
    palette=paleta_customizada, # Aplicamos a nossa paleta customizada
    edgecolor='black', # Borda fina para destaque
    linewidth=1 # Espessura da borda
)


# --- 5. FORMATAÇÃO EXECUTIVA (Rótulos e Títulos) ---
plt.title('Revenue Performance by Canadian City - Company C', fontsize=18, fontweight='bold', pad=25)
plt.xlabel('City', fontsize=13)
# Omitimos o rótulo do eixo Y, pois vamos colocar os valores nas barras
plt.ylabel('', fontsize=0) 

# Rotacionar um pouco os nomes das cidades
plt.xticks(rotation=15, fontsize=11)


# --- ✨ MÁGICA SENIOR: Rótulos de Valor nas Barras (Bar Labels) ✨ ---
# Iteramos sobre cada barra para adicionar o texto customizado
for bar in chart.patches:
    # Obtém a altura da barra (o valor financeiro)
    height = bar.get_height()
    
    # Formata o valor como moeda canadense (C$ 1,234.56)
    valor_formatado = f"C${height:,.2f}"
    
    # Adiciona o texto (rótulo) diretamente acima da barra
    chart.annotate(
        valor_formatado, # Texto a ser exibido
        xy=(bar.get_x() + bar.get_width() / 2, height), # Posição: (centro da barra, topo)
        xytext=(0, 7), # Pequeno ajuste fino (deslocamento) para o texto não colar na barra
        textcoords="offset points", # Sistema de coordenadas relativo
        ha='center', # Alinhamento horizontal centralizado
        va='bottom', # Alinhamento vertical na base (do texto)
        fontsize=11, # Tamanho da fonte do rótulo
        fontweight='bold', # Negrito para destacar
        color='black' # Cor do texto
    )


# --- 6. FORMATAÇÃO FINAL ---
# Remove as linhas de grade que podem poluir a imagem
sns.despine(left=True, bottom=False) # Remove a linha lateral e mantém a inferior

# Ajuste fino para nada sair cortado na imagem final
plt.tight_layout()


# --- 7. SALVANDO O RESULTADO (O Arquivo de Saída) ---
nome_imagem = 'grafico_faturamento_company_c_REFINADO.png'
plt.savefig(nome_imagem, dpi=300) # dpi=300 garante alta resolução

print(f"\n--- SUCESSO ---")
print(f"O gráfico executivo REFINADO foi gerado e salvo como: {nome_imagem}")
print("Verifique a barra lateral esquerda para ver o novo arquivo de imagem.\n")