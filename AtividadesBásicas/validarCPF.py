cpf = input('CPF: ')

separar1_cpf = cpf.split('-')
separar2_cpf = separar1_cpf[0].split('.')
juntar_cpf = ''.join(separar2_cpf)

soma = 0

for indice, contador in enumerate(range(10, 1, -1)):
    aux_int = int(juntar_cpf[indice])
    soma += aux_int * contador

form = 11 - (soma % 11)

if form > 9 :
    digito1 = '0'
else:
    digito1 = str(form)

lista_cpf = [juntar_cpf, digito1]
juntar2_cpf = ''.join(lista_cpf)
# print(juntar2_cpf)

soma = 0

for indice, contador in enumerate(range(11, 1, -1)):
    aux_int = int(juntar2_cpf[indice])
    soma += aux_int * contador

form = 11 - (soma % 11)

if form > 9 :
    digito2 = '0'
else:
    digito2 = str(form)

lista_cpf.append(digito2)
lista_digitos = [digito1, digito2]
digitos = ''.join(lista_digitos)

if digitos == separar1_cpf[1]:
    print('CPF validado!')
else:
    print('CPF cancelado!')