matriz = [ # e1 e2 e3 e4 (arestas)
    [1, 1, 0, 0], # Nó 1
    [1, 0, 1, 0], # Nó 2
    [0, 1, 1, 1], # Nó 3
    [0, 0, 0, 1] # Nó 4
]

contador = []

print(f'  |e1|e2|e3|e4|')
for l in range(4):
    grau = 0
    lista_auxliar = []

    print(f' {l + 1}|', end = '')
    for c in range(4):
        if matriz[l][c] == 1 :
            print(f' {matriz[l][c]}|', end = '')
            grau += 1
        
        if matriz[l][c] == 0 :
            print(f' {matriz[l][c]}|', end = '')
    print()
    contador.append(grau)

for i in range(4):
    print(f'Grau do nó {i + 1} = {contador[i]}')
