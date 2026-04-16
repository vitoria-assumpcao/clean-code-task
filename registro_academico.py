class RegistroAcademico:
    """Representa o registro acadêmico de um aluno."""

    def __init__(self, nome_aluno: str, numero_matricula: int, eh_bolsista: bool):
        """
        Inicializa o registro acadêmico do aluno.

        @param nome_aluno: nome completo do aluno
        @param numero_matricula: número de matrícula (deve ser positivo)
        @param eh_bolsista: indica se o aluno possui bolsa de estudos
        """
        self.nome_aluno = nome_aluno
        self.numero_matricula = numero_matricula
        self._eh_bolsista = eh_bolsista

    @property
    def nome_aluno(self) -> str:
        """Retorna o nome do aluno."""
        return self._nome_aluno

    @nome_aluno.setter
    def nome_aluno(self, valor: str):
        """Define o nome do aluno. Não pode ser vazio."""
        if not valor or not valor.strip():
            raise ValueError("Nome do aluno não pode ser vazio.")
        self._nome_aluno = valor.strip()

    @property
    def numero_matricula(self) -> int:
        """Retorna o número de matrícula do aluno."""
        return self._numero_matricula

    @numero_matricula.setter
    def numero_matricula(self, valor: int):
        """Define o número de matrícula. Deve ser positivo."""
        if valor <= 0:
            raise ValueError("Número de matrícula deve ser positivo.")
        self._numero_matricula = valor

    @property
    def eh_bolsista(self) -> bool:
        """Retorna se o aluno é bolsista."""
        return self._eh_bolsista

    def calcula_mensalidade(self, valor_base: float):
        """
        Calcula e exibe a mensalidade do aluno.
        Bolsistas pagam 50% do valor base.
        @param valor_base: valor cheio da mensalidade
        """
        if self._eh_bolsista:
            print(f"Mensalidade: {valor_base / 2}")
        else:
            print(f"Mensalidade: {valor_base}")

    def mostra_registro(self):
        """Exibe os dados do registro acadêmico do aluno."""
        print(f"Nome: {self._nome_aluno}")
        print(f"Matricula: {self._numero_matricula}")
        print(f"Bolsista: {self._eh_bolsista}")