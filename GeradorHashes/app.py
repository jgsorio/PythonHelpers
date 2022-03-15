import hashlib

string = input('Digite o texto a ser gerado: ')
hash = int(input('Escolha qual o tipo da criptografia: 1 - MD5, 2 - SHA1, 3 - SHA256, 4 - SHA512: '))

string = string.encode('utf-8')

if hash == 1:
    result = hashlib.md5(string).hexdigest()
    print(f'A hash gerada: {result}')
elif hash == 2:
    result = hashlib.sha1(string).hexdigest()
    print(f'A hash gerada: {result}')
elif hash == 3:
    result = hashlib.sha256(string).hexdigest()
    print(f'A hash gerada: {result}')
elif hash == 4:
    result = hashlib.sha512(string).hexdigest()
    print(f'A hash gerada: {result}')
else:
    print('A escolha não existe')
