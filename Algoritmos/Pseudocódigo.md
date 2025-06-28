1. Imprimir um número em tela
    Inicio
        Escreva ("Digite um numero")
        Leia num
        Escreva ("Você digitou: ", num)
    Fim
2. Somar dois números
    Inicio
        Escreva ("Digite o primeiro valor")
        Leia num1
        Escreva ("Digite o segundo valor")
        Leia num2
        soma = num1 + num2
        Escreva ("A soma dos valores é: ", soma)
    Fim
3. Contar de 1 até 10 usando loop
    Inicio
        num = 0
        Enquanto num for menor ou igual a dez 10:
            Escreva (num)
            num = num + 1
    Fim
4. Verificar se o número é par ou ímpar
    Inicio
        Escreva ("Escreva um numero: ")
        Leia num
        Se o resto da divisão num / 2 = 0:
            Escreva("O numero é par")
        Se não:
            Escreva ("O numero é par")
5. Verificar se número é positivo, negativo ou zero
    Inicio
        Escreva ("Digite um numero: ")
        Leia num
        Se num > 0:
            Escreva ("O numero é positivo")
        Se num < 0:
            Escreva ("O numero é negativo")
        Se não:
            Escreva ("O numero vale zero")
    Fim
6. Calcular média de 3 notas
    Inicio
        Escreva ("Digite a nota 1: ")
        Leia nota1
        Escreva ("Digite a nota 2: ")
        Leia nota2
        Escreva ("Digite a nota 3: ")
        Leia nota3
        media = (nota1 + nota2+ nota3)/3
        Escreva ("A media das notas vale: ", media)
    Fim
7. Verificar se aluno foi aprovado (com média ≥ 5)
    Inicio
        Leia nota
        Se nota for maior ou igual a 5:
            Escreva ("aprovado")
        Se não:
            Escreva ("reprovado")
8. Maior entre dois números
    Inicio
        Leia num1
        Leia num2
        Se num1 - num2 < 0:
            Escreva("O numero 2 é maior que o numero 1")
        Se num1 - num2 > 0:
            Escreva("O numero 1 é maior que o numero 2")
        Se não:
            Escreva ("Os numeros são iguais")
9. Mostrar os múltiplos de 3 até 30
    Inicio
        x = 3
        n = 2
        Mostre 3
        Enquanto x <= 30:
            x = x * n
            n+1
            Mostre x
    Fim
10. Contagem regressiva de 10 até 1
    Inicio
        x = 10
        Enquanto x != 0:
            Mostre x
            x - 1
    Fim