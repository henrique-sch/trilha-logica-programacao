# sao tres linhas e tres colunas com espaços em brancos
# vai ser apontado a posicao e onde o jogador digitar é substituido pelo valor
# tres listas com os espaços dos numeros

# tabuleiro = [[' ' for i in range(3)] for i in range(3)]

print(tabuleiro)
faopkf

tabuleiro = [
    ['00', '01', '02'],
    ['10', '11', '12'],
    ['20', '21', '22']
]

print(tabuleiro[0])
print(tabuleiro[1])
print(tabuleiro[2])
proxima = True
while proxima:
    jogadores = ['X', 'O']
    for jogador in jogadores:
        jogada = input(f'Digite a posição que deseja jogar {jogador}: ')
        tabuleiro[int(jogada[0])][int(jogada[1])] = jogador
        n = 0
        for linha in tabuleiro:
            print(tabuleiro[n])
            n += 1

        for linha in tabuleiro:
            if all(elm == 'X' for elm in linha):
                print('O jogador X venceu!')
                proxima = False
            elif all(elm == 'O' for elm in linha):
                print('O jogador O venceu!')
                proxima = False
        for elm in range(3):
            if tabuleiro[0][elm] == 'X' and tabuleiro[1][elm] == 'X' and tabuleiro[2][elm] == 'X':
                print('O jogador X venceu!')
                proxima = False
            if tabuleiro[0][elm] == 'O' and tabuleiro[1][elm] == 'O' and tabuleiro[2][elm] == 'O':
                print('O jogador O venceu!')
                proxima = False
    