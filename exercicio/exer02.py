perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

p1 = input(perguntas[0]['Pergunta'] + '\n' + 'Opções: ' + str(perguntas[0]['Opções']) + '\n')

if p1 == perguntas[0]['Resposta']:
    print('Acertou!')
else:
    print('Errou!')

p2 = input(perguntas[1]['Pergunta'] + '\n' + 'Opções: ' + str(perguntas[1]['Opções']) + '\n')

if p2 == perguntas[1]['Resposta']:
    print('Acertou!')
else:
    print('Errou!')    

'''

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

'''    