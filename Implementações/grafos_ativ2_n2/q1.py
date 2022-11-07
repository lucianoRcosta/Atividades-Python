'''
Matriz de adjacência 
Eu escolhi a matriz da dois, mas n dirigida
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

for i in range(n):
    lista_aux = []
    for j in range(n):
        if grafo[i][j] == 1 and i == 0:
            lista_aux.append(j + 1)

        if grafo[i][j] == 1 and i == 1:
            lista_aux.append(j + 1)
        
        if grafo[i][j] == 1 and i == 2:
            lista_aux.append(j + 1)
        
        if grafo[i][j] == 1 and i == 3:
            lista_aux.append(j + 1)
        
        if grafo[i][j] == 1 and i == 4:
            lista_aux.append(j + 1)
        
    lista_adj.append(lista_aux)

cont = 0
for l in lista_adj:
    cont+= 1
    print(f'{cont} | -> {l}')    
