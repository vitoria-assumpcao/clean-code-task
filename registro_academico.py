class RegistroAcademico:

    def __init__(self, nome_aluno: str, numero_matricula: int, eh_bolsista: bool):
        self.nome_aluno = nome_aluno
        self.numero_matricula = numero_matricula
        self.eh_bolsista = eh_bolsista
        self.mensalidade = 0.0
        self.desconto = 0.0

    def calcula_mensalidade(self, valor_base: float):
        if self.eh_bolsista == True:
            self.mensalidade = valor_base / 2
            print(f"Mensalidade: {self.mensalidade}")
        else:
            self.mensalidade = valor_base
            print(f"Mensalidade: {self.mensalidade}")

    def mostra_registro(self):
        print(f"Nome: {self.nome_aluno}")
        print(f"Matricula: {self.numero_matricula}")
        print(f"Bolsista: {self.eh_bolsista}")