sequência = int(input("Quantos números tem a sua sequência? "))

soma = 0
i = 0

while i < sequência:
	número = int(input("Digite um número: "))
	soma = soma + número
	i = i + 1

print("a soma é", soma)