import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

np = [
    {**p,  'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

#print(produtos)
#print(np)


ordena_produtos = sorted(np, key=lambda p: p['nome'], reverse=True  ) 
print(ordena_produtos)
print('-------------------')

ordena_produtos = sorted(np, key=lambda p: p['preco'])
print(ordena_produtos)