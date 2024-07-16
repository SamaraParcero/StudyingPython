print("Digite sua nota")
nota = float(input("Sua nota:"))
notaFormatada = round(nota, 1)
print(notaFormatada)
if (10> notaFormatada>6):
   print("Você passou de ano")
elif(notaFormatada<4) :
   print("Você não passou de ano")
elif  4<= notaFormatada <6 :
   print("Você está em prova final")
else :
   print("Nota inválida")