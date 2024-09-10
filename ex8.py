notas = []
x = 0
i = 0

while len(notas) < 4:
    notas.extend(input("insera uma nota: "))
    x = sum(notas[i], x)
    i = i + 1

if x/4 >= 7:
    print("Aprovado")
else:
    notas.extend(input("insera a nota da prova final: "))
    x = sum(x, notas[i])

    if x/5 >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
