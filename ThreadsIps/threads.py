from ast import arg
from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Carro 1: {piloto} - {trajeto}')
        trajeto += velocidade
        time.sleep(0.5)

t_carro1 = Thread(target=carro, args=[1, 'José'])
t_carro2 = Thread(target=carro, args=[1.5, 'Ana'])

t_carro1.start()
t_carro2.start()