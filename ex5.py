kwh = float(input("Selecione o número de kw/h"))

consumo = kwh * 0.56

geracaoEnergia = consumo * (41/100)
imposto = consumo * (22.52/100)


bandeira = input("Qual a bandeira tarifária em vigor (Amarela, Vermelha1, Vermelha2)? ").lower()

if bandeira == "amarela":
    adicional = kwh * 0.015
elif bandeira == "vermelha1":
    adicional = kwh * 0.040
elif bandeira == "vermelha2":
    adicional = kwh * 0.060
else:
    adicional = 0.0
    print("Bandeira não reconhecida. Adicional será zero.")

valorConta = geracaoEnergia + imposto + consumo + adicional

print(valorConta)