meucartão = int(input("Digite o número do seu cartão de credito: "))

cartãolido = 1
encontreimeucartãonalista = False

while cartãolido !=0 and not encontreimeucartãonalista:
	cartãolido = int(input("Digite o número do próximo cartão de crédito: "))
	if cartãolido == meucartão:
		encontreimeucartãonalista = True

if encontreimeucartãonalista:
	print("Eba! Meu cartão está lá!")
else:
	print("Xi, meu cartão não está lá!")