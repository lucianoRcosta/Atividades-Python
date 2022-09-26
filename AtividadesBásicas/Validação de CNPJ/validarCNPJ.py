"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

def formatarCNPJ(cnpj_completo): # Função que checa se o formato do cnpj está correto e retira os sinais
    
    if len(cnpj_completo) == 18 and '/' in cnpj_completo and '-' in cnpj_completo and '.' in cnpj_completo:
        lista_separar = cnpj_completo.split('/')
        var_juntar = ''.join(lista_separar)

        lista_separar = var_juntar.split('-')
        var_juntar = ''.join(lista_separar)
        
        lista_separar = var_juntar.split('.')
        var_juntar = ''.join(lista_separar)

        return var_juntar[:-2]
    else:
        pass

def checagemInput(cnpj_completo): # Função que checa se cnpj possui apenas números
    try:
        aux_checagem = int(cnpj_completo)
        return aux_checagem
    except ValueError:
        pass
    except TypeError:
        pass

def digito1(cnpj): # Função que faz o cálculo do digito 1
    mult_aux1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    cnpj_aux = ''
    for i, valor in enumerate(cnpj):
        mult_aux1[i] *= int(valor) 
        soma += mult_aux1[i]
    
    soma = 11 - (soma % 11)

    if soma > 9:
        soma = 0 
    
    cnpj_aux = [cnpj, str(soma)]
    cnpj = ''.join(cnpj_aux)

    return cnpj

def digito2(cnpj): # Função que faz o cálculo do digito 2
    mult_aux1 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    cnpj_aux = ''
    for i, valor in enumerate(cnpj):
        mult_aux1[i] *= int(valor) 
        soma += mult_aux1[i]
    
    soma = 11 - (soma % 11)

    if soma > 9:
        soma = 0 
    
    cnpj_aux = [cnpj, str(soma)]
    cnpj = ''.join(cnpj_aux)

    return cnpj

def refazerCPNJ(digito2):
    lista = []
    for valor in digito2:
        lista.append(valor)

    lista.insert(2, '.')
    lista.insert(6, '.')
    lista.insert(10, '/')
    lista.insert(15, '-')
    nova_string = ''.join(lista)
    return nova_string

def validar(cnpj_completo, digito2): # Função de validação
    if cnpj_completo == digito2:
        return 'Válido!'
    else:
        return 'Inválido!'

if __name__ == '__main__':
    cnpj_completo = '40.688.134/0001-61'
    cnpj_digitos = refazerCPNJ(digito2(digito1(formatarCNPJ(cnpj_completo))))
    # print(refazerCPNJ(cnpj_digitos))
    print(cnpj_digitos)
    print(validar(cnpj_completo, cnpj_digitos))