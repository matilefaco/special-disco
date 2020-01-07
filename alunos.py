alunos = int(input("Digite o número de alunos: "))
notas = 1
total_recup = 0


while notas <= alunos:
	nota_aluno = int(input("Digite aqui uma nota entre 0 e 10: "))
	if nota_aluno > 3 and nota_aluno < 5:
		total_recup = total_recup + 1
	notas = notas + 1
	

print("A quantidade de alunos de recuperação é", total_recup)