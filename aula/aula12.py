arquivo = 'C:\\Users\\styven\\Desktop\\Python\\aula\\'
arquivo += 'aula1.txt'

#cria o arquivo e escreve dentro dele
with open(arquivo, 'a+', encoding='utf-8') as arquivo:
    a =+ 1
    arquivo.write( 'Escrevendo no arquivo com Pythonççççç\n')
    arquivo.writelines('Escrevendo no arquivo com Python\n ')
    print(f'arquivo fechado', {a})
    arquivo.seek(0,0) 
    print(arquivo.read())   


