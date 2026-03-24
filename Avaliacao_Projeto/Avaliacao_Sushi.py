# SENAC - AVALIAÇÃO (PROJETO TANOSHIMI: DIVISÃO DE FUNÇÕES)
# CAIO - ADD_ITEM_PEDIDO ()
# → REGSITRA A ESCOLHA DO CLIENTE NA LISTA DE ITENS CONSUMIDOS NA MESA.


# EXEMPLO DA IDEIA
# def adicionar_item(lista, item):
#     lista.append(item)

# minha_lista = [1, 2, 3]
# adicionar_item(minha_lista, 4)

# print(minha_lista)
#______________________________________________________
# FORMA DE LISTA 
def add_item_pedido (lista, item):
    lista.append(item)

lista_de_pedidos = ["Temaki", "Teriaki", "Sushi"]
add_item_pedido(lista_de_pedidos, "Hot Philadelphia")

print(lista_de_pedidos)                                                                      
#______________________________________________________
# FORMA DE DICIONARIO

MESA_01 = {
    'Pedido 1':'Sushi',
    'Pedido 2':'Sashimi',
    'Pedido 3':'Salmão'}

def add_item_lista (lista, pedido, item):
    lista [pedido] = item

add_item_lista(MESA_01, 'Pedido 4','Hot Philadelphia')
add_item_lista(MESA_01, 'Pedido 5','Molho Teriyaki')
add_item_lista(MESA_01, 'Pedido 6','Ramen Completo')

print (MESA_01)

 
# explicação
#[] no dicionário → acessa pela chave
# = → define ou atualiza o valor
# informacao[chave] = valor → cria ou altera um item