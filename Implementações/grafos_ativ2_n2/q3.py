'''
Grafo Ciclo
Eu escolhi o grafo da dois, mas n dirigido
e um grafo na forma de polígono de 6 lados
'''

def grafo_ciclo(N, grafo):
    lista_adj = []

    cont_linha = 0
    aux = 0
    for i in range(N):
        lista_aux = []
        for j in range(N):
            if grafo[i][j] == 1 and i == cont_linha:
                lista_aux.append(j + 1)
                aux += 1
            
        lista_adj.append(lista_aux)
        cont_linha += 1

    cont = 0
    for l in lista_adj:
        cont+= 1
        print(f'{cont} | -> {l}')  

    if N*2 == aux:
        cont = 0
        check = True
        cont_linha = 0
        for i in lista_adj:    
            cont += 1
            for j in i:
                if ((j == cont + 1 or j == cont + (N - 1)) or (j == cont - 1 or j == cont - (N - 1))) and (cont == 1 or cont == N):
                    continue
                else:
                    if (j == cont - 1 or j == cont + 1) and (cont != 1 and cont != N):
                        continue
                    else:
                        check = False

        if check == True:
            print('Grafo Ciclo')
        else:
            print('Não é Grafo Ciclo !')   
            
    else:
        print('Não é um grafo ciclo !')

# Aqui é o main

grafo1 = [
[0,1,0,1,1], # nó 1
[1,0,0,1,0], # nó 2
[0,0,0,1,0], # nó 3
[1,1,1,0,1], # nó 4
[1,0,0,1,0]  # nó 5
]

grafo2 = [
[0,1,0,0,0,1], # nó 1
[1,0,1,0,0,0], # nó 2
[0,1,0,1,0,0], # nó 3
[0,0,1,0,1,0], # nó 4
[0,0,0,1,0,1], # nó 5
[1,0,0,0,1,0]  # nó 6
]


grafo3 = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    ]

n1 = 5
n2 = 6
n3 = 4

grafo_ciclo(n1, grafo1)
grafo_ciclo(n2, grafo2)
grafo_ciclo(n3, grafo3)
