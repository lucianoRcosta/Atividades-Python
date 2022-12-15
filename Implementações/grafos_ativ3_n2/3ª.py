def grafo_roda(grafo):
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

    check_grau3 = 0
    check_nmenos1 = 0
    cont = 0

    for i in range(nmr_vert):
        if graus[i] == 3:
            check_grau3 += 1

        if graus[i] == (nmr_vert - 1):
            check_nmenos1 +=1
        
        cont += 1
        print(f'Número de graus do vértice {cont}: {graus[i]}')
    
    if check_grau3 == (nmr_vert - 1) and check_nmenos1 == 1:
        print('Grafo é roda!')
    else:
        print('Grafo não é roda!')
    
    print()

#MAIN
grafo1 = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    ]

grafo2 = [
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,1,0,1,1],
    [1,0,1,0,1],
    [1,1,1,1,0],
    ]

grafo3 = [
    [0,1,0,0,1,1],
    [1,0,1,0,0,1],
    [0,1,0,1,0,1],
    [0,0,1,0,1,1],
    [1,0,0,1,0,1],
    [1,1,1,1,1,0],
    ]

grafo_roda(grafo1)
grafo_roda(grafo2)
grafo_roda(grafo3)
