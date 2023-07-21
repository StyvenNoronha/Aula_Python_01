import os
arquivo = 'C:\\Users\\styven\\Desktop\\Python\\aula'
arquivo += 'aula2.txt'


#le o arquivo
with open(arquivo, 'a+') as arq:
    arq.write('Escrevendo no arquivo com Python\n')
    arq.seek(0,0) 
    print(arq.read())

os.rename(arquivo, 'aulastyven.txt')
#os.unlink(arquivo)       
#os.remove(arquivo)       