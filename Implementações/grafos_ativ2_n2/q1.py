'''
Matriz de adjacência 
Eu escolhi o grafo da dois, mas n dirigido
'''

grafo = [
[0,1,0,1,1], # nó 1
[1,0,0,1,0], # nó 2
[0,0,0,1,0], # nó 3
[1,1,1,0,1], # nó 4
[1,0,0,1,0]  # nó 5
]

n = 5

lista_adj = []

a = 0
for i in range(n):
    lista_aux = []
    for j in range(n):
        if grafo[i][j] == 1 and i == a:
            lista_aux.append(j + 1)
        
    lista_adj.append(lista_aux)
    a += 1

cont = 0
for l in lista_adj:
    cont+= 1
    print(f'{cont} | -> {l}')    
