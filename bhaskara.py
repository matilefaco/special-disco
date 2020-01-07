a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = float(input("Qual é o valor de c? "))

delta = (((b * b) - (4 * a * c)))
raizdelta = (delta ** (1/2))


if delta == 0:
	raiz1 = (-b + raizdelta) / (2 * a)
	print("a raiz desta equação é", raiz1)
else:
	if delta < 0:
		print("esta equação não possui raízes reais")
	else:
		raiz1 = (-b + raizdelta) / (2 * a)
		raiz2 = (-b - raizdelta) / (2 * a)
		if raiz1 > raiz2:	
			print("as raízes da equação são", raiz2, "e", raiz1)
		if raiz2 > raiz1:
			print("as raízes da equação são", raiz1, "e", raiz2)