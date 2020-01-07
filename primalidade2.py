número = int(input("Digite um número inteiro: "))

divisor = 2
primo = True

while (divisor < número and primo):
	primo = not ((número % divisor) == 0)
	divisor = divisor + 1

if primo and número != 1:
	print("primo")
else:
	print("não primo")