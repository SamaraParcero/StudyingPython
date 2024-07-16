num1 = float(input("Digite um valor: "))
num2 = float(input("Digite um valor: "))
num3 = float(input("Digite um valor: "))


numeros = [num1, num2, num3]

print("Lista original:", numeros)


for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[i]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada:", numeros)