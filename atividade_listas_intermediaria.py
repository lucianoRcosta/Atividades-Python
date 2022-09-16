"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

lista_retorno = []

for i1, v1 in enumerate(lista_de_listas_de_inteiros):  
    var_i3 = 0

    lista_checar = []
    lista_comparar = []
    lista_comparar += v1
    
    for i2, v2 in enumerate(v1):
        # print(i2, v2)
        alpha = 0 

        for i3, v3 in enumerate(lista_comparar):
            # print(f'{v2}[{i2}] -> {v3}[{i3}]')
            if var_i3 == 0:
                if v2 == v3 and i2 != i3 and alpha == 0 :
                    var_i3 = i3
                    # print(var_i3)
                    # print(v2, v3)
                    # lista_checar.append(v2)
                    alpha += 1
                
            else:
                if v2 == v3 and var_i3 > i3 and alpha == 0 and not(v2 in lista_checar) and i2 != i3:
                    var_i3 = i3
                    # print(var_i3)
                    # print(v2, v3)
                    # lista_checar.append(v2)
                    alpha += 1

        lista_checar.append(v2)
    
    if var_i3 == 0:    
        lista_retorno.append(-1)
    else:
        lista_retorno.append(v1[var_i3])
        # print(v1[var_i3])
       
    
print(lista_retorno)