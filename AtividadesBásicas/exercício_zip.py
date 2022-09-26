lista1 = [4, 5, 6, 8, 10]
lista2 = [7, 9, 11, 13, 15, 48, 96, 192, 384, 768]

lista_junta = zip(lista1, lista2)
lista_soma = [x + y for x, y in lista_junta]

# lista_soma = [x + y for x, y in zip(lista1, lista2)] # versão corrigida
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # possível situação em que fosse pedido para fazer a soma com base na 
# maior lista

print(lista_soma)