números = int(input("Digite um inteiro grande: "))

soma = 0

while números > 0:
	resto = números % 10
	números = números // 10
	soma = soma + resto

print("a soma dos dígitos é", soma)