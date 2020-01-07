número1 = int(input("Digite aqui o primeiro número inteiro: "))
número2 = int(input("Digite aqui o segundo número inteiro: "))
número3 = int(input("Digite aqui o terceiro número inteiro: "))


if (número3 >= número2) and (número2 >= número1):
	print("crescente")
else:
	print("não está em ordem crescente")