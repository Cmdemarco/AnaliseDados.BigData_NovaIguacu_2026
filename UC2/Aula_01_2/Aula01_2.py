# PROCESSO DE ROTINA 
import pandas as pd

df_transacoes = pd.read_excel('C:\\Users\\caio.pais\\Downloads\\base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('C:\\Users\\caio.pais\\Downloads\\base_invest.xlsx', sheet_name='Ativo')

# Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações? ---
# variável nova    tabela[filtro]
df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
#
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']
print(df_compra)
print(df_venda)


max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()

print("--- Preços máximos e mínimos das operações ---")
print(f"Preço máximo de compra: {max_compra_preco}")
print(f"Preço mínimo de compra: {min_compra_preco}")
print(f"Preço máximo de venda: {max_venda_preco}")
print(f"Preço mínimo de venda: {min_venda_preco}")
print("\n")

