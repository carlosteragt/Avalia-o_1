def fibonaci_sequence(N):
    x = 0
    sequencia = [0,1]

    while len(sequencia) != 7:
        x = sequencia[(len(sequencia) - 2)]
        x = x + sequencia[len(sequencia) - 1]
        sequencia.insert(len(sequencia) + 1, x)
        x = 0
    return sequencia

def main():
    N = input("insera um valor: ")
    fibonaci_sequence(N)
    print(f'A sequencia de fibonacci com {N} termos é: {fibonaci_sequence(N)}')

main()
