anterior = float(input("primeiro: "))
proximo = 1
decrescente = True

while proximo > 0 and decrescente:
	proximo = float(input("próximo: "))
	if proximo > anterior:
		decrescente = False

if decrescente:
	print("Sim, é uma sequência de números decrescente :-)")
else:
	print("Não, não é uma sequência de números decrescente :-(")