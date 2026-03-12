# IF, ELIF AND ELSE
# carro = False
# combustivel = False



#  if not carro and not combustivel:
#      print ("Meu carro está funcionando.")
#  else:
#      print ("Vish, deu ruim")






# if carro==True and combustivel==True:
#     print ("Meu carro está funcionando.")
# elif carro==False or combustivel==False:
#     print ("Vish, deu ruim")
# else:
#     print ("Erro de execução")

# semana = int(input("Informe seu dia:"))
# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")

# MATCH CASE
# mes = int(input("Digite seu mês:"))
# match mes:
#  case 1:
#     print("Janeiro")
#  case 2:
#     print("Fevereiro")
#  case 3:
#     print("Março")
#  case 6:
#     print("Junho")
#  case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#     print("Mês inválido")

# try:
#     numero_mes = int(input("Digite um número de 1 a 12:"))

#     match numero_mes:
#         case 1:
#             print("O número 1 corresponde a Janeiro.")
#         case 2:
#             print("O número 1 corresponde a Fevereiro.")
#         case 3:
#             print("O número 1 corresponde a Março.")
#         case 4:
#             print("O número 1 corresponde a Abril.")
#         case 5:
#             print("O número 1 corresponde a Maio.")
#         case 6:
#             print("O número 1 corresponde a Junho.")
#         case 7:
#             print("O número 1 corresponde a Julho.")
#         case 8:
#             print("O número 1 corresponde a Agosto.")
#         case 9:
#             print("O número 1 corresponde a Setembro.")
#         case 10:
#             print("O número 1 corresponde a Outubro.")
#         case 11:
#             print("O número 1 corresponde a Novembro.")
#         case 12:
#             print("O número 12 corresponde a Dezembro.")
#         case _:
#             print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")
# except ValueError:
#             print("Entrada inválida. Por favor, digite um número inteiro.")
# except IndentationError:
#             print("Código Invalido. Esqueceu a identação")

        
intervalo = range(10)
print(intervalo)

print('***')

for numero in range (10):
    print('número:')
    print(numero)
