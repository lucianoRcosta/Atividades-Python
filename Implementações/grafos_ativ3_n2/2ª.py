def grafo_regular(grafo):
    graus = []
    check = 0
    nmr_vert = 0
    # esse for conta os graus dos nós
    for c in grafo:
        aux = 0
        nmr_vert += 1
        for l in c:
            if l == 1:
                aux += 1
        
        graus.append(aux)

    cont = 0
    check = 0
    # checa se os graus são iguais
    for i in range(nmr_vert):
        for j in range(nmr_vert):
            if graus[i] != graus[j]:
                check = 1

        cont += 1
        print(f'Número de graus do vértice {cont}: {graus[i]}')

    if check == 0: 
        print('Grafo regular !')
        print()
    else:
        print('Grafo não é regular !')
        print()

#MAIN
grafo1 = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    ]

grafo2 = [
    [1,1,0,1],
    [1,1,1,0],
    [1,1,1,1],
    [1,0,1,0],
    ]

grafo3 = [
    [0,1,1,0,1],
    [1,1,1,0,0],
    [0,1,1,1,0],
    [0,0,1,1,1],
    [1,0,0,1,1],
    ]

grafo_regular(grafo1)
grafo_regular(grafo2)
grafo_regular(grafo3)

