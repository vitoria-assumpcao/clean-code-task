class RegistroAcademico:
 
    def __init__(self, nomeAluno: str, numeroMatricula: int, ehBolsista: bool):
        self.nomeAluno = nomeAluno
        self.numeroMatricula = numeroMatricula
        self.ehBolsista = ehBolsista
        self.mensalidade = 0.0
        self.desconto = 0.0
 
    def calculaMensalidade(self, valorBase: float):
        if self.ehBolsista == True:
            self.mensalidade = valorBase / 2
            print(f"Mensalidade: {self.mensalidade}")
        else:
            self.mensalidade = valorBase
            print(f"Mensalidade: {self.mensalidade}")
 
    def mostraRegistro(self):
        print(f"Nome: {self.nomeAluno}")
        print(f"Matricula: {self.numeroMatricula}")
        print(f"Bolsista: {self.ehBolsista}")
 