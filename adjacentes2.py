númerosalvo = n = int(input("Digite um número inteiro: "))

anterior = n % 10
n = n // 10
adjacente = False
prox = 0

while n > 0 and not adjacente:
	atual = n % 10
	if atual == anterior:
		adjacente = True
	else:
		prox += 1
	anterior = atual
	n = n // 10

if adjacente:
	print("sim")
else:
	print("não")