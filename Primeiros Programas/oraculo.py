import time
print('Olá, sou sua assistente eletronica, vou te guitar pelos assuntos de consulta !')
time.sleep(1)
print('Por favor digite um dos assuntos possiveis:')
print('1. I.A'+'\n'+'2. Dados'+'\n'+'3. SQL'+'\n'+'4. Web')
entrada = input()

match entrada:
    case '1':
        print("""Inteligência Artificial (IA) é uma área da computação que desenvolve sistemas capazes de realizar tarefas que normalmente exigiriam
        inteligência humana, como aprender, raciocinar, reconhecer padrões
        e tomar decisões.""")
    case '2':
        print("""Dados são informações brutas, como números, 
        textos ou medições, que podem ser coletadas, processadas e analisadas para gerar conhecimento e apoiar na tomada de decisões.""")
    case '3':
        print("""SQL (Structured Query Language) é uma linguagem padrão usada para gerenciar e manipular bancos de dados relacionais. 
        Com SQL, é possível consultar, inserir, atualizar e excluir dados, além de criar e alterar estruturas de tabelas e bancos.""")
    case '4':
        print("""Web, ou World Wide Web, é um sistema que permite o acesso e a navegação de documentos e conteúdos através da internet, 
        usando navegadores (como Chrome, Firefox ou Safari). Ela é composta por páginas interligadas por 
        links e estruturadas com tecnologias como HTML, CSS e JavaScript, que formam a base da experiência visual e interativa na internet.""")