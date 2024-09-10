def ler_cpf(cpf):
    x = 0
    cpf.replace(".", "")
    cpf.replace("-", "")
    for i in cpf:
        x = x + cpf[i]
    return i

def main():
    cpf = (input("insera seu cpf nesse formato 999.999.999-99: "))
    par_ou_impar = ler_cpf(cpf)
    print(par_ou_impar // 2)
    if par_ou_impar // 2 != 0:
        print("par")
    else:
        print("impar")

main()