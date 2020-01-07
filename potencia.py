# calcula a potência de n e k, com k >= 0

def main():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))

    pot = 1
    i   = 0
    while i < k:
        pot = pot * n
        i   = i + 1

    print("A potencia é", pot)  # print mais simples
    print("O valor de %d elevado a %d é %d" %(n, k, pot)) # mais elaborado


#--------------------------------------------
main()