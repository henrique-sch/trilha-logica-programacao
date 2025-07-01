import time, random

cores = [
    "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "rosa", "marrom", "preto", "branco",
    "cinza", "ciano", "magenta", "limão", "verde-petróleo", "índigo", "violeta", "ouro", "prata", "bege",
    "coral", "carmesim", "azul-escuro", "verde-escuro", "vermelho-escuro", "caqui", "lavanda", "bordô",
    "marinho", "oliva", "orquídea", "ameixa", "salmão", "sépia", "azul-céu", "cinza-ardósia", "bronzeado",
    "cardo", "tomate", "turquesa", "trigo", "azul-claro", "creme-de-hortelã", "marfim", "mel"
]

print('Pense em uma cor...')
time.sleep(1)
print('Pensando...')
time.sleep(2)
gerador = random.randint(0, len(cores))
print(f'Você pensou na cor: {cores[gerador]}')
