time1 = 0
time2 = 0
time3 = 0
time4 = 0

time1 = int(input("Digite a quantidade de gols que o time 1 fez"))
time2 = int(input("Digite a quantidade de gols que o time 2 fez"))
time3 = int(input("Digite a quantidade de gols que o time 3 fez"))
time4 = int(input("Digite a quantidade de gols que o time 4 fez"))

if time1 == time2 :
    p1= int(input("insira o número de acertos nos penultimos do time1(0 a 5)"))
    p2 =  int(input("insira o número de acertos nos penultimos do time2(0 a 5)"))
    if p1>p2 :
        print("time1 é o vencedor")
    else :
        print("time2 é o vencedor")

if time3 == time4 :
    p3= int(input("insira o número de acertos nos penultimos do time3(0 a 5)"))
    p4 =  int(input("insira o número de acertos nos penultimos do time4(0 a 5)"))
    if p3>p4 :
        print("time3 é o vencedor")
    else :
        print("time4 é o vencedor")


if time1 > time2 & time3>time4:
    print("time 1 e time3 são finalistas")
elif time1<time2 & time3>time4:
    print("time 2 e 3 são finalistas")
elif time1>time2 & time3<time4 :
    print("time 1 e 4 são finalistas")
else:
    print("time 2 e 4 são finalistas")


