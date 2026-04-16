from registro_academico import RegistroAcademico

aluno = RegistroAcademico("Breno", 55555, False)

mensalidade = aluno.calcula_mensalidade(4000.0)
print(f"Mensalidade: {mensalidade}")

registro = aluno.mostra_registro()
print(f"Nome: {registro['nome']}")
print(f"Matricula: {registro['matricula']}")
print(f"Bolsista: {registro['bolsista']}")