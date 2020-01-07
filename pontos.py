x1 = float(input("Digite aqui o valor de x: "))
y1 = float(input("Digite aqui o valor de y: "))
x2 = float(input("Digite aqui o segundo valor de x: "))
y2 = float(input("Digite aqui o segundo valor de y: "))

distância = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)) ** (1/2)

if distância >= 10:
	print("longe")
if distância < 10:
	print("perto")