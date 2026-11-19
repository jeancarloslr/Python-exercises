print("Escreva abaixo um número")
number = int(input())

cont = 1
soma = 0

while cont <= number:

    soma += cont
    cont += 1

print("A soma acumulada do número digitado é de: ", soma)