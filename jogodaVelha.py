jogador = 'X'
def exibeTabuleiro():
    for linha in tabuleiro:
        print(f'{linha[0]} | {linha[1]} | {linha[2]}')

def jogada(linha, coluna):
    if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'O':
        print('Posição inválida')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

tabuleiro = [
    ['00', '01', '02'],
    ['10', '11', '12'],
    ['20', '21', '22']
]

exibeTabuleiro()


proxima = True
while proxima:
    linha_coluna = input(f'Digite a posição que deseja jogar {jogador}: ')
    try:
        jogador = jogada(int(linha_coluna[0]), int(linha_coluna[1]))
    except ValueError:
        print('Os valores devem ser numeros inteiros')
    except IndexError:
        print('Digite uma posição válida')
    n = 0
    exibeTabuleiro()

    for linha in tabuleiro:
        if all(elm == 'X' for elm in linha):
            print('O jogador X venceu!')
            proxima = False
        elif all(elm == 'O' for elm in linha):
            print('O jogador O venceu!')
            proxima = False
    for elm in range(3):
        if (
        tabuleiro[0][elm] == 'X' and 
        tabuleiro[1][elm] == 'X' and 
        tabuleiro[2][elm] == 'X'):
            print('O jogador X venceu!')
            proxima = False
        if (
        tabuleiro[0][elm] == 'O' and 
        tabuleiro[1][elm] == 'O' and 
        tabuleiro[2][elm] == 'O'):
            print('O jogador O venceu!')
            proxima = False
    if (
        tabuleiro[0][0] == 'X' and 
        tabuleiro[1][1] == 'X' and 
        tabuleiro[2][2] == 'X'
        ) or (
            tabuleiro[0][2] == 'X' and 
            tabuleiro[1][1] == 'X' and 
            tabuleiro[2][0] == 'X'
            ):
        print('O jogador X venceu')
        proxima = False
    if (
        tabuleiro[0][2] == 'O' and 
        tabuleiro[1][1] == 'O' and 
        tabuleiro[2][0] == 'O'
        ) or (
            tabuleiro[0][0] == 'O' and 
            tabuleiro[1][1] == 'O' and 
            tabuleiro[2][2] == 'O'
            ):
        print('O jogador O venceu')
        proxima = False
    cont_empate = 0
    for linha in tabuleiro:
        if all(elm in ('X', 'O') for elm in linha):
            cont_empate += 1
    if cont_empate == 3:
        print('Jogo finalizado')
        proxima = False
