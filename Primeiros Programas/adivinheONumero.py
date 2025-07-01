import time, random

print('Pense em um numero de 1 até 10 !!!')
time.sleep(1)
print('Pensando...')
time.sleep(2)
gerador = random.randint(1, 10)
print(f'Você pensou no: {gerador} !!! ')