class RegistroAcademico:

    def __init__(self, nome_aluno: str, numero_matricula: int, eh_bolsista: bool):
        self._nome_aluno = nome_aluno
        self._numero_matricula = numero_matricula
        self._eh_bolsista = eh_bolsista

    @property
    def nome_aluno(self) -> str:
        return self._nome_aluno

    @property
    def numero_matricula(self) -> int:
        return self._numero_matricula

    @property
    def eh_bolsista(self) -> bool:
        return self._eh_bolsista

    def calcula_mensalidade(self, valor_base: float):
        if self._eh_bolsista == True:
            print(f"Mensalidade: {valor_base / 2}")
        else:
            print(f"Mensalidade: {valor_base}")

    def mostra_registro(self):
        print(f"Nome: {self._nome_aluno}")
        print(f"Matricula: {self._numero_matricula}")
        print(f"Bolsista: {self._eh_bolsista}")