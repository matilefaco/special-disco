# soma de números inteiros diferentes de zero, até um deles ser zero.

def main():
    num = int(input("Digite um inteiro: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))

    print("A soma é", soma)

main()