número = int((input("Digite um número inteiro grande: "))

soma = 0

i = 0

while i // 10 > 0:
	i = i + número % 10
	soma = soma + número // 10


print("a soma é", soma)