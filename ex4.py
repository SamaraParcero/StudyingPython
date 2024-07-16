salarioMensal = float(input("Digite seu sálario mensal"))
salarioAnual = salarioMensal*12

valorMax = 28559.70

if salarioAnual >= valorMax:
    print("Você precisa pagar imposto de renda")
else :
    print("Você não precisa pagar imposto de renda")