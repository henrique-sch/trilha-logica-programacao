import random, time

qa_list = [
    ["O que é Python?", 
     "Sistema operacional", 
     "Linguagem de programação",       # correta: b
     "Banco de dados", 
     "Navegador web",
     "b"],
    
    ["O que é IA?", 
     "Simulação de inteligência humana",  # correta: a
     "Sistema de armazenamento", 
     "Tipo de hardware", 
     "Linguagem de programação",
     "a"],
    
    ["Para que serve HTML?", 
     "Estilizar páginas web", 
     "Gerenciar banco de dados", 
     "Controlar versões",
     "Estruturar páginas web",        # correta: d
     "d"],
    
    ["O que é SQL?", 
     "Linguagem de marcação", 
     "Sistema operacional", 
     "Linguagem para bancos de dados",  # correta: c
     "Editor de texto",
     "c"],
    
    ["O que é variável?", 
     "Comando de repetição", 
     "Banco de dados",
     "Tipo de função", 
     "Armazena valores",              # correta: d
     "d"],
    
    ["O que é loop?", 
     "Linguagem de programação", 
     "Estrutura condicional",
     "Repetição de código",           # correta: c
     "Tipo de dado", 
     "c"],
    
    ["Para que serve CSS?", 
     "Criar bancos de dados", 
     "Programar robôs", 
     "Estilizar páginas web",          # correta: c
     "Gerenciar servidores",
     "c"],
    
    ["O que é algoritmo?", 
     "Editor de texto", 
     "Sistema operacional",
     "Passos para resolver problemas", # correta: c
     "Banco de dados", 
     "c"],
    
    ["O que é back-end?", 
     "Interface do usuário", 
     "Lógica no servidor",             # correta: b
     "Programa para editar imagens", 
     "Linguagem de marcação",
     "b"],
    
    ["O que é front-end?", 
     "Interface do usuário",           # correta: a
     "Banco de dados", 
     "Sistema operacional", 
     "Tipo de loop",
     "a"],
]

pontuacao = 0
print('Vamos jogar um jogo')
continuar = True
while continuar:
    if len(qa_list) == 0:
        print('Acabaram as perguntas')
        continuar = False
    print('Responda a seguinte pergunta...'+'\n')
    gerador = random.randint(0, len(qa_list)-1)
    time.sleep(1)
    print(qa_list[gerador][0])
    print('a. '+qa_list[gerador][1])
    print('b. '+qa_list[gerador][2])
    print('c. '+qa_list[gerador][3])
    print('d. '+qa_list[gerador][4]+'\n')
    resposta_usuario = input('Digite a resposta: ')
    if resposta_usuario == qa_list[gerador][5]:
        pontuacao += 1
        print('Acertou')
    else:
        print('Errou')
    print(f'Sua pontuação é: {pontuacao}')
    qa_list.pop(gerador)
