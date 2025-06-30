x = 5 # Variavel global
def soma():
    x = 10 # Variavel local
    print(x)
    return x + 1
soma()
print(x)

def multiplicaDoisNumeros(a, b = 1):
    return a * b

print(multiplicaDoisNumeros(5))