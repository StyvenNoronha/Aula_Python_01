arquivo = 'C:\\Users\\styven\\Desktop\\Python\\aula\\'
arquivo += 'aula.txt'

#cria o arquivo e escreve dentro dele
with open(arquivo, 'w') as arquivo:
    #arquivo.write('Escrevendo no arquivo com Python\n')
    arquivo.write('Escrevendo no arquivo com Python\n')
    print('arquivo fechado')   



#le o arquivo
with open(arquivo, 'w+') as arquivo:
    #arquivo.write('Escrevendo no arquivo com Python\n')
    #arquivo.write('Escrevendo no arquivo com Python\n')
    print(arquivo.read())
    print('arquivo fechado')   


'''
# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
'''     