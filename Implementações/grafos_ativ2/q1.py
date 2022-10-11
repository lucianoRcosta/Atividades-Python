matriz = [
    [0, 0, 0, 0, 0, 0, 0,-1], # Nó 2
    [0, 0, 0, 0, 1, 0, 1, 0], # Nó 3
    [0, 0, 0, 0, 0, 0, 0, 1], # Nó 5
    [0, 0, 0, 0, 1, 0, 0, 1], # Nó 7
    [0,-1, 0,-1, 0, 1, 0, 0], # Nó 8
    [0, 0, 0, 0, 1, 0, 0,-1], # Nó 9
    [0,-1, 0, 0, 0, 0, 0,-1], # Nó 10
    [1, 0,-1,-1, 0, 1, 1, 0], # Nó 11
]

lista_v = [2, 3, 5, 7, 8, 9, 10, 11] #lista dos nós

contador = [] # lista para o grau de entrada e saída

print(f'  | 2| 3| 5| 7| 8| 9|10|11|')

for l in range(8): # for da linha
    ce = 0 # contador do grau de entrada
    cs = 0 # contador do grau de saída
    
    if l < 6: # checagem para o espaçamento da string
        print(f'{lista_v[l]} |', end='') # índice da lateral da matriz
    else:
        print(f'{lista_v[l]}|', end='')  # índice da lateral da matriz  
    
    for c in range(8): # for dos valores da linha
        if matriz[l][c] == 1 :
            print(f' {matriz[l][c]}|', end = '')
            cs += 1
        
        if matriz[l][c] == -1 :
            print(f'{matriz[l][c]}|', end = '')
            ce += 1 

        if matriz[l][c] == 0 :
            print(f' {matriz[l][c]}|', end = '')

    contador.append(f'Grau de Entrada: {ce} e Grau de Saída: {cs}')
    print()

for i in range(8): # Esse for printa o grau de entrada e saída
    print(f'Grau do nó {lista_v[i]} = {contador[i]}')
        
