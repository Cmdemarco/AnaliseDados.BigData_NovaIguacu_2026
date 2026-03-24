# Atividades Práticas
# 1.1) Controle de Pesca
# Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
# traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
# pagar uma multa de R$ 4,00 por quilo excedente.
# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.


def calcular_multa(peso_total):
    limite = 100
    if peso_total > limite:
        excesso = peso_total - limite
        multa = excesso * 4
        return multa
    else:
        return 0.0


total_multa = 0.0

while True:
    peso = float(input("Digite o peso dos peixes (0 para encerrar): "))

    if peso == 0:
        break

    multa = calcular_multa(peso)

    if multa > 0:
        print(f"Multa a pagar: R$ {multa:.2f}")
        total_multa += multa
    else:
        print("Peso dentro do limite. Nenhuma multa a pagar.")

print(f"\nTotal de multas acumuladas: R$ {total_multa:.2f}")


# 2.1) Calculadora de IMC
# Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
# pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
# ● Fórmula: IMC = PESO / (ALTURA * ALTURA)
# ● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
# os valores e retornará o IMC calculado.
# ● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
# valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
# ○ Valores de Referência:
# ■ Menor que 18.5: "Abaixo do peso"
# ■ 18.5 a 24.9: "Peso normal"
# ■ 25.0 a 29.9: "Sobrepeso"
# ■ 30.0 ou mais: "Obesidade"
# ● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
# chamar as duas funções e imprimir o resultado formatado.

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


def obter_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


# Programa principal
n = int(input("Quantas pessoas deseja calcular o IMC? "))

for i in range(n):
    print(f"\nPessoa {i+1}")

    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = calcular_imc(peso, altura)
    classificacao = obter_classificacao(imc)

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")


# 3.1) Conversor de Temperatura
# Crie um programa que permita ao usuário converter temperaturas entre Celsius e
# Fahrenheit.
# ● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
# temperatura em Celsius e retorna o valor em Fahrenheit.
# ○ Fórmula: F = (C * 9/5) + 32
# ● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
# temperatura em Fahrenheit e retorna o valor em Celsius.
# ○ Fórmula: C = (F - 32) * 5/9
# ● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
# "1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
# resultado.
# Desafio: Criar uma única função que faça qualquer uma das conversões,
# sempre perguntando ao usuário qual é desejada

def celsius_para_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32


def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5/9


# Programa principal
print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha a opção (1 ou 2): ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = celsius_para_fahrenheit(c)
    print(f"Resultado: {f:.2f}°F")

elif opcao == "2":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = fahrenheit_para_celsius(f)
    print(f"Resultado: {c:.2f}°C")

else:
    print("Opção inválida!")



# Atividades Práticas Part 2
# 1.2) Verificador de Ano Bissexto
# Crie uma função chamada eh_bissexto(ano):
# ● A função deve receber um ano (inteiro) como parâmetro.
# ● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
# ● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
# menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
# e 2100 não são).
# ● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
# "O ano X NÃO é bissexto", baseado no retorno da função.


def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


# Programa principal
ano = int(input("Digite um ano: "))

if eh_bissexto(ano):
    print(f"O ano {ano} É bissexto")
else:
    print(f"O ano {ano} NÃO é bissexto")


# 2.2) Contagem de Caracteres
# Crie uma função chamada contar_caractere(texto, caractere_procurado):
# ● A função deve receber uma string texto e uma string caractere_procurado (de um só
# caractere).
# ● Ela deve retornar o número de vezes que o caractere_procurado aparece no texto.
# (Não diferencie maiúsculas de minúsculas!)
# ● Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres.
# ● No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado
# da contagem.

def contar_caractere(texto, caractere_procurado):
    contador = 0

    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()

    for letra in texto:
        if letra == caractere_procurado:
            contador += 1

    return contador


# Programa principal
frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

resultado = contar_caractere(frase, caractere)

print(f"O caractere '{caractere}' aparece {resultado} vezes.")



# 3.3) Simulador de Dado
# Usando o módulo random, crie uma função rolar_dado(lados).
# ● A função deve receber o número de lados do dado (ex: 6, 10, 20).
# ● Ela deve retornar um número aleatório entre 1 e o número de lados (use
# random.randint(1, lados)).
# ● No programa principal, crie um "simulador de batalha":
# ○ Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função
# rolar_dado(20).
# ○ Peça ao usuário para "Rolar para o Dano (d8)". Chame a função
# rolar_dado(8).
# ○ Imprima os resultados de cada rolagem.

import random


def rolar_dado(lados):
    return random.randint(1, lados)


# Programa principal
input("Pressione ENTER para Rolar para o Ataque (d20)...")
ataque = rolar_dado(20)
print(f"Resultado do Ataque: {ataque}")

input("\nPressione ENTER para Rolar para o Dano (d8)...")
dano = rolar_dado(8)
print(f"Resultado do Dano: {dano}")