crescente = True

sequência = int(input("Digite a quantidade de números da sua sequência "))

anterior = int(input("Digite um número da sequência "))

valor = 0


while valor <= sequência and crescente:
	valor = int(input("Digite outro número da sequência "))
	if anterior > valor:
		crescente = False

if crescente == True:
	print("Está em ordem crescente.")
else:
	print("Não está em ordem crescente.")