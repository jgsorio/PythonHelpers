import itertools

string = input('Digite a palavra a ser permutada: ')

resultado = itertools.permutations(string, len(string))

for word in resultado:
    print(''.join(word))
