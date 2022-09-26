carrinho = []

carrinho.append(('Produto 1', 45))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 10))

carrinho_total = [v[1] for v in carrinho]

print(sum(carrinho_total)) # função sum => soma todos os valores da lista