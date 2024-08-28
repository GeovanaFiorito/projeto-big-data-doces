script_content = """
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar as planilhas
df_estoque = pd.read_excel('data/controle_estoque_doces_personalizados.xlsx')
df_financeiro = pd.read_excel('data/controle_financeiro.xlsx')
df_vendas = pd.read_excel('data/controle_vendas_mensal.xlsx')

# Cálculo de quantidade vendida
df_vendas['Quantidade Vendida'] = df_vendas['Material Usado (R$)'] / df_estoque.set_index('Nome do Item')['Preço Unitário (R$)']

# Atualizando o estoque
df_estoque['Estoque Atual'] = df_estoque['Quantidade em Estoque'] - df_vendas.set_index('Descrição')['Quantidade Vendida']

# Custo Total por Venda
df_vendas['Custo Total (R$)'] = df_vendas['Material Usado (R$)'] + df_vendas['Mão de Obra (R$)']

# Lucro Bruto
df_vendas['Lucro Bruto (R$)'] = df_vendas['Valor Final (R$)'] - df_vendas['Custo Total (R$)']

# Preparação para os gráficos
sns.set(style='whitegrid')

# Gráfico de Barras: Estoque Atual vs. Quantidade Inicial
plt.figure(figsize=(10,6))
sns.barplot(x='Nome do Item', y='Estoque Atual', data=df_estoque, color='blue')
plt.title('Estoque Atual por Item')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/estoque_atual_por_item.png')
plt.show()

# Gráfico de Linhas: Receita vs. Despesas Mensais
df_financeiro_mes = df_financeiro.groupby(df_financeiro['Data'].str[:7]).sum()
df_vendas_mes = df_vendas.groupby(df_vendas['Data'].str[:7]).sum()

plt.figure(figsize=(10,6))
plt.plot(df_vendas_mes.index, df_vendas_mes['Valor Final (R$)'], label='Receita')
plt.plot(df_financeiro_mes.index, df_financeiro_mes['Valor (R$)'], label='Despesas')
plt.title('Receita vs. Despesas Mensais')
plt.legend()
plt.tight_layout()
plt.savefig('images/receita_vs_despesas_mensais.png')
plt.show()

# Gráfico de Pizza: Distribuição de Custos
plt.figure(figsize=(8,8))
df_vendas.groupby('Descrição')['Custo Total (R$)'].sum().plot.pie(autopct='%1.1f%%')
plt.title('Distribuição de Custos por Venda')
plt.tight_layout()
plt.savefig('images/distribuicao_de_custos.png')
plt.show()

# Geração do Relatório Final em Planilha
df_resumo = pd.DataFrame({
    'Item': df_estoque['Nome do Item'],
    'Estoque Inicial': df_estoque['Quantidade em Estoque'],
    'Estoque Atual': df_estoque['Estoque Atual'],
    'Receita Total (R$)': df_vendas.groupby('Descrição')['Valor Final (R$)'].sum(),
    'Lucro Bruto Total (R$)': df_vendas['Lucro Bruto (R$)'].sum()
})
df_resumo.to_excel('data/resumo_final_projeto.xlsx', index=False)
"""

# Especificando o caminho para salvar o script
file_path_script = '/mnt/data/analise_dados.py'

# Salvando o conteúdo no arquivo
with open(file_path_script, 'w') as file:
    file.write(script_content)

file_path_script
