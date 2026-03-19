# Atividades Práticas

# Use if/elif/else e/ou match/case para resolver os desafios abaixo:
# 1. Cálculo de Lâmpadas:
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.

try:
    potencia= int(input("Informe a potencia:")) # usuário declarando as variáveis necessárias para a execução
    largura= int(input("Informe a largura:")) # usuário declarando as variáveis necessárias para a execução
    comprimento= int(input("Informe o comprimento:"))  #usuário declarando as variáveis necessárias para a execução
    dimensao= 3 * 3 #parte do verificador.

    if potencia>=3 and dimensao==9: # verificação de condição => verdadeira
        print("1 lampada ilumina o comodo") # Retorno da condição verdadeira
    elif potencia>=3 and dimensao<9: #verificação de condição => falsa.
        print("precisa de mais uma lampada/bocal por comodo") # Retorno da condição falsa
    elif potencia<3 and dimensao==9: #verificação de condição => falsa
        print("potencia insuficiente") # Retorno da condição falsa.
    else: #Nenhuma das condições atendidas.
        print("Potencia e dimensões insuficientes!") #retorno da exceção
except:
    print("Erro desconhecido!")




# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²


comprimento= float(input("Informe o comprimento: "))
largura= float(input("Informe a largura: "))
altura= float(input("Informe a altura: "))
perimetro= 2 * (comprimento + largura)
area_paredes= perimetro * altura
q_caixas= area_paredes/1.5

if q_caixas >=0 and area_paredes >=0:
    print(f"quantidade de caixas: {q_caixas:.2f}")
else:
    print("Os valores são inválidos")



# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

combustivel= 6.15
odometro_inicio = float(input("Informe a marcação do odometro do inicio do dia (em KM):"))
odometro_final = float(input("Informe a marcação do odometro do final do dia (em KM):"))
combustivel_gasto = float(input("Informe a quantidade de litros de combustivel gastos:"))
valor_recebido = float(input("Informe o valor total recebido pelos passageiros (em R$):"))

km_percorridos = odometro_final - odometro_inicio #distancia percorrida
media_consumo = km_percorridos / combustivel_gasto
custo_combustivel = combustivel_gasto * combustivel
lucro_liq = valor_recebido - custo_combustivel


# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:

# Codigo_01 = "Sul"
# Codigo_02 = "Norte"
# Codigo_03 = "Leste"
# Codigo_04 = "Oeste"
# Codigo_05 = "Nordeste"
# Codigo_06 = "Nordeste"
# Codigo_07 = "Sudeste"
# Codigo_08 = "Sudeste"
# Codigo_09 = "Sudeste"
# Codigo_10 = "Centro Oeste"
# Codigo_11 = "Noroeste"

# Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# encarado como “Importado”.

codigo=5

match codigo:
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5:
        print("Nordeste")
    case 6:
        print("Nordeste")
    case 7:
        print("Sudeste")
    case 8:
        print("Sudeste")
    case 9:
        print("Sudeste")
    case 10:
        print("Centro-Oeste")
    case 11:
        print("Noroeste")
    case _:
        print("Importado")

# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0

# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final.

nota1= float(input("Digite a nota da primeira prova"))
nota2= float(input("Digite a nota da segunda prova"))
opt= abs(float(input("Digite a nota da optativa:")))

if opt != -1:
    if nota1 < nota2:
        nota1 = opt  
    else:
        nota2 = opt  

media = (nota1 + nota2) / 2

if media >= 6.0:
    resultado = "Aprovado"
elif media < 3.0:
    resultado = "Reprovado"
else:
    resultado = "Recuperação"

print(f"\nMédia final: {media:.1f}")
print(f"Situação: {resultado}")

# 6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo.

Numero = int(input("Digite seu número:"))

if Numero >= 0:
    print ("Seu número é positivo")
else:
    print ("Seu número é negativo")
