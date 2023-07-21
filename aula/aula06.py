lista = [
    {'nome': 'João', 'idade': 25, 'nota': 9.5,},
    {'nome': 'Maria', 'idade': 27, 'nota': 8.5,},
    {'nome': 'José', 'idade': 30, 'nota': 7.5,},
    {'nome': 'Paulo', 'idade': 28, 'nota': 6.5,},
    {'nome': 'Ana', 'idade': 26, 'nota': 5.5,},
    {'nome': 'Carlos', 'idade': 29, 'nota': 4.5,},
]

# Ordenando a lista por nome
'''
def ordena(item):
    return item['nome']

lista.sort(key=ordena)
for i in lista:
    print(i)

# Ordenando a lista por nome de outra forma
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['nota'], reverse=True)

def exibir(lista):
    for i in lista:
        print(i)

exibir(l1)
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
exibir(l2)
'''

def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)