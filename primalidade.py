número = int(input("Digite um número inteiro: "))

divisor = 0

while divisor <= número:
	divisor = divisor + 1
	if (número % divisor != 0) and (divisor != número) and (divisor != 1):
		primo = True 
	else:
		primo = False


if primo:
	print("primo")
else:
	print("não primo")