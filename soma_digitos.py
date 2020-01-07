número = int(input("Digite um número inteiro: "))

soma = 0

while número > 0:
	resto = número % 10
	número = número // 10
	soma = soma + resto

print(soma)