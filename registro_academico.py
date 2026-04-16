class RegistroAcademico:

    def __init__(self, nome_aluno: str, numero_matricula: int, eh_bolsista: bool):
        self.nome_aluno = nome_aluno
        self.numero_matricula = numero_matricula
        self.eh_bolsista = eh_bolsista

    def calcula_mensalidade(self, valor_base: float):
        if self.eh_bolsista == True:
            print(f"Mensalidade: {valor_base / 2}")
        else:
            print(f"Mensalidade: {valor_base}")

    def mostra_registro(self):
        print(f"Nome: {self.nome_aluno}")
        print(f"Matricula: {self.numero_matricula}")
        print(f"Bolsista: {self.eh_bolsista}")