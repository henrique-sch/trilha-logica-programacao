import random, time

print('Adivinhe o numero de 1 até 10')
gerador = random.randint(1,10)
print(gerador)
while True:
    tentativa = int(input('Digite o numero: '))
    if tentativa == gerador:
        print('Voce Acertou !')
        break
    else:
        print('Voce errou')