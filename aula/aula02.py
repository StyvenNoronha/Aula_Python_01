def criar_sau(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


s1 = criar_sau('Olá')
s2 = criar_sau('Bom dia')
print(s1('João'))

for nome in ['Ana', 'Carlos', 'Daniel']:
    print(s2(nome))

