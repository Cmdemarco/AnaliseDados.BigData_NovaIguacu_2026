# RANGE
# intervalo = range(10)
# print(intervalo)

# print('***')

# for numero in range (10):
#     print('número:')
#     print(numero)


# for i in range(5):
#     try:
#         # i representa o número atual da repetição (0, 1, 2...)
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))

#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4

#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

# >>>>>> WHILE
# Loolap = 400
# while Loolap > 300:
#     Loolap = float (input('Qual o valor do evento (inteira)?'))
#     print("Negativo.")

# print("Estarei lá")


############################################
nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']
print(nomes)
# nome1 = nomes[0]

# print(nomes[-1])
# print(nomes[-2])
# print(nomes[-3])
# print(nomes[-4])
# print(nome1)

# primeira_parte=nomes[0:3]
# print(primeira_parte)
# segunda_parte=nomes[3:6]
# print(segunda_parte)

# print(len(nomes))

#TUPLAS:
nomes_tupla=tuple(nomes)
print(nomes_tupla)
#SETS:
nomes_set=set(nomes)
print(nomes_set)
#DICIONÁRIOS:
nomes_dict={1:'Matheus',
            2: 'Alice',
            3: 'Caio',
            4: 'Larissa',
            5:'Miguel',
            6: 'Rafael'}


nomes_att = ["Daniela Sabino", "Rafael Portugal", "Sergio Cabral"]
sobrenome = []
# dani = nomes_att [0][8:]
# rafael = nomes_att [1][7:]
# sergio = nomes_att [2][6:]
# sobrenome = [dani,rafael,sergio]
# print (sobrenome)

for i in nomes_att:
    sobrenome .append(nomes_att[0])
print (sobrenome)

nome5='Luciene'
nome4= 'Miguel'
nomes_att.insert(2, nome4)
nomes_att.append(nome5)
nomes_att.append(nome5)

nomes_att.count(2)
print(nomes_att)




############ LISTAS

lista01=[100,20,43,23,675,23,12,55]
#           [0]    [1] [2]  [3] ...
for i in lista01:
    print(i,':',type(i))

print(lista01[-1][2])


## TUPLAS ###

pares=(40,20,2,18,14,34,96,30,20,58)
print(pares[3])
print(pares[3:])
print(pares[3:8])
print(len(pares))
pares=pares+(44,)
print(pares)
lista_pares=list(pares)
print(lista_pares)
lista_pares.append(102)
lista_pares.sort()
lista_pares=tuple(lista_pares)
print(lista_pares)

### SETS ###
impares={33,5,17,11,27,11,71,79,99,15}
print(impares)
print(type(impares))
impares_02={11,3,23,83,15,73}
intersecao=impares.intersection(impares_02)
print(intersecao)

# DICIONÁRIO: Usando o índice como chave (ex: 1: 'Filme A')
dicionario_filmes = {}
for i in range(len(dados_entrada)): # Repetição pelo tamanho da lista
 # Usando o índice (i+1) como CHAVE e o nome como VALOR
 dicionario_filmes[i + 1] = dados_entrada[i]
print(f"LISTA (Flexível): {lista_filmes}")
print(f"TUPLA (Fixa): {tupla_filmes}")
print(f"SET (Apenas Únicos): {set_filmes}")
print(f"DICIONÁRIO (Chave: Valor): {dicionario_filmes}")
