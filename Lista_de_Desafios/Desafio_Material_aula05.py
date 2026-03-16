# Desafios
# 1. Cálculo de Média Escolar para Vários Alunos
# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

for i in range (1, 11):
    print(f"aluno {i}")

    b1 = float(input("Informe a nota do 1º bimestre:"))
    b2 = float(input("Informe a nota do 2º bimestre:"))
    b3 = float(input("Informe a nota do 3º bimestre:"))
    b4 = float(input("Informe a nota do 3º bimestre:"))

    media=(b1+b2+b3+b4)/4

    if media >=6:
        status="Aprovado"
    elif media >=5:
        status= "Recuperação"
    else:
        status= "Reprovado"
    print(f"media do aluno:{media}, condição:{status}")

# 2. Cadastro de Candidatos
# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.
# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.

contador=0
limite=12

while contador < limite:
    ano=int(input("informe o ano de nascimento:"))
    idade =2026-ano
    if idade < 18:
        print("participação negada")
    else:
        telefone=int(input("Informe um telefone de contato:"))
        email=str(input("Informe o seu email:"))
    contador= contador + 1

# 3. Tentativa de Login e Senha
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio.

contador=0
limite=3
usuario="admin"
codigo=1234

while contador < limite:
    login=str(input("digite o login:"))
    senha=int(input("digite a senha:"))

    if login==usuario and senha==codigo:
        print("Login realizado com sucesso!")
        break
    else: 
        contador=contador + 1
        chances= limite - contador
        if chances > 0:
            print(f"Usuario ou senha invalidos! chances restantes:{chances}")
else:
        print("limite atingido!")