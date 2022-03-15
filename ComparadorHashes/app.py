import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash01 = hashlib.new('ripemd160')
hash02 = hashlib.new('ripemd160')

# Ler o arquivo em modo binario
hash01.update(open(arquivo1, 'rb').read())
hash02.update(open(arquivo2, 'rb').read())

if hash01.digest() != hash02.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print('Os arquivos são iguais')
    print(f'Hash do arquivo a.txt é: {hash01.hexdigest()}') # Mostra o hash usando hexdecimal
    print(f'Hash do arquivo b.txt é: {hash02.hexdigest()}')
