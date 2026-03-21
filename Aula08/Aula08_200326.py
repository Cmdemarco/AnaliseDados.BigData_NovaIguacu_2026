# Coleta de Dados
# dados_entrada = []
# print ("Digite 5 noms de filme:")
# for i in range(5):
#     nome= input(f"filme {i+1}: " )
#     dados_entrada.append(nome) 

# print ('-' * 30)
# lista_de_filmes = dados_entrada
# print (lista_de_filmes)

#_____________________________________________

# def somar(a, b):
#     resultado = a + b
#     return resultado

# somar1= somar (5,10)
# soma2 = somar (100,50)

#_____________________________________________

import random

def gerar_dados (qtd, min_val, max_val):

    for _ in range (qtd):
        lista_de_dados = random.randint (min_val, max_val)
        

    return lista_de_dados

# Testanto a função
dados_aleatorios = gerar_dados (1, 1, 20)
print (f"D20: {dados_aleatorios}")