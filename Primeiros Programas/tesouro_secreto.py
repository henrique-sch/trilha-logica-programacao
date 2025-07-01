
import time

def exibeTabuleiro():
    for linha in tabuleiro_usuario:
        print(f'{linha[0]} | {linha[1]} | {linha[2]}| {linha[3]}')

def jogada(linha, coluna):
    tabuleiro_usuario[linha][coluna] = tabuleiro_real[linha][coluna]
    return tabuleiro_real[linha][coluna]

tabuleiro_usuario = [
    ['00','01','02','03'],
    ['10','11','12','13'],
    ['20','21','22','23'],
    ['30','31','32','33']
]

tabuleiro_real = [
    ['X','X','X','X'],
    ['X','X','💎','X'],
    ['X','X','X','X'],
    ['X','X','X','X']
]
print('Encontre o tesouro!!!')
time.sleep(1)
exibeTabuleiro()
proxima = True
while proxima:
    linha_coluna = input('Digite a posicao que deseja jogar: ')
    try:
        tentativa = jogada(int(linha_coluna[0]), int(linha_coluna[1]))
    except (IndexError, ValueError):
        print('Digite um valor válido de posição')
        tentativa = 'X'
    if tentativa == '💎':
        exibeTabuleiro()
        print('Voce ganhou !')
        break
    exibeTabuleiro()

