def grafo_euleriano(grafo):
    #contador de vertices e arestas
    vert = 0
    for g in grafo:
        aresta = 0
        vert += 1
        for l in g:
            aresta += 1
    
    #contador dos gruas
    graus = []
    for g in grafo:
        print(g) 
        aux_graus = 0
        for c in g:
            if c == 1:
                aux_graus += 1
        graus.append(aux_graus)
    
    print()

    #checagem dos graus
    cont_vert = 0
    check = 0 
    for grau in graus:
        cont_vert += 1
        print(f'Grau do vértice {cont_vert}: {grau}')
       
        if grau % 2 == 1 or grau == 0:
            check += 1
    
    print()

    if check != 0:
        print('Grafo possui um ou mais vértices ímpares!')
        print()
        return
    else:
        print('Grafo com grau par!')
        print()
    
    lista_pos = [] #uma lista com posições
    for c in range(aresta):
        lista_aux = []
        for l in range(vert):
            if grafo[l][c] == 1:
                lista_aux.append(l)
        
        lista_pos.append(lista_aux)
    
    # for p in lista_pos:
    #     print(p) 
    lista_aux = []
    aux = 0
    cont = 0
    for l in range(aresta):
        aux1 = lista_pos[l][0]
        aux2 = lista_pos[l][1]
        for c in range(vert):
            
        
    
    print()



    # lista_inc = []
    # a = 0 # auxiliar de comparação
    # for l in range(vert):
    #     lista_aux = []
    #     for c in range(aresta):
    #         if grafo[l][c] == 1 and l == a:
    #             lista_aux.append(c)
            
    #     lista_inc.append(lista_aux)
    #     a += 1
    
    # cont = 0
    # for l in lista_inc:
    #     cont+= 1
    #     print(f'{cont} | -> {l}')   

    # for c1 in lista_inc:
    #     for c2 in lista_inc:


#main
#matriz de incidência
#vértice = linha & coluna = aresta

grafo1 = [
    [1,0,0,0,1],
    [1,1,0,0,0],
    [0,1,1,0,0],
    [0,0,1,1,0],
    [0,0,0,1,1]
]

grafo2 = [
    [1,1,0,0,0,0,0],
    [1,0,1,0,0,0,0],
    [0,1,0,1,0,0,0],
    [0,0,1,1,1,1,0],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1]
]

grafo3 = [
    [1,1,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,1],
]

grafo_euleriano(grafo1)
grafo_euleriano(grafo2)
grafo_euleriano(grafo3)

