# Desafios (ugprade)

# Média Escolar para 5 Estudantes
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().

#Criando a lista vazia
resultados = []
for i in range (1, 6): 
    nota1=int(input("informe a primeira nota: ")) 
    nota2=int(input("informe a segunda nota: "))
    media=(nota1+nota2)/2    
    if media <4:
        resultados.append(f"Aluno {i} - Reprovado (Media:{media})")
    elif media >=4 and media <6:
        resultados.append(f"Aluno {i} - Recuperacao (Media:{media})")
    else:
        resultados.append(f"Aluno {i} - Aprovado (Media:{media})")
    print(resultados[-1])


# EXERCICIO 2
# Cadastro Seletivo de Candidatos
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato).

candidatos_validos = []
for i in range (1,6):
    if int(input("informe a sua idade: ")) < 18:
        print(f"Rejeitado")
    else: 
        candidato = {
            'candidato': i,
            'nome': str(input("informe o seu nome: ")),
            'email': str(input("informe o seu email: "))
        }
        candidatos_validos.append(candidato)
    print(candidatos_validos)

# def add_candidatos (lista, candidatos, nomes):
#     lista [candidatos] = nomes

# add_candidatos (Lista_candidato, 'Candidato 4','Luiza')
# add_candidatos (Lista_candidato, 'Candidato 5','Heloize')
# add_candidatos (Lista_candidato, 'Candidato 6','Otávio')
# add_candidatos (Lista_candidato, 'Candidato 7','Raissa')

# print (Lista_candidato)