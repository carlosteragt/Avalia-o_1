
def calcular_soma_quadrados(vetor):
    x = 0
    for i in vetor:
        x = x + i**2
    return x

        
def main():
    vetor_A = [1,2,3,4,5,6,7,8,9,10]
    print(calcular_soma_quadrados(vetor_A))
    

main()