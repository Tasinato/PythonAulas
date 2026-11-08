"""Versão 3: validação orientada a objetos de senhas com regras de composição.

Use apenas entradas fictícias. A aprovação não mede a segurança real de uma senha.
"""

CARACTERES_ESPECIAIS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
SENHAS_BLOQUEADAS = {"password", "12345678", "qwerty"}
class ValidadorSenha:
    """Reúne a configuração das regras e o comportamento de validação."""

    def __init__(self, tamanho_minimo=8, tamanho_maximo=20):
        if not 1 <= tamanho_minimo <= tamanho_maximo:
            raise ValueError("Os limites devem satisfazer 1 <= mínimo <= máximo.")
        self.tamanho_minimo = tamanho_minimo
        self.tamanho_maximo = tamanho_maximo
        self.caracteres_especiais = CARACTERES_ESPECIAIS
        self.senhas_bloqueadas = SENHAS_BLOQUEADAS.copy()

    def obter_regras(self):
        """Retorna as regras para apresentar ao usuário."""
        return (
            f"Conter entre {self.tamanho_minimo} e {self.tamanho_maximo} caracteres.",
            "Conter pelo menos uma letra maiúscula.",
            "Conter pelo menos uma letra minúscula.",
            "Conter pelo menos um número.",
            "Conter pelo menos um caractere especial da lista: " + self.caracteres_especiais,
            "Não conter espaços em branco, tabulações ou quebras de linha.",
            "Ser diferente de 'password', '12345678' e 'qwerty' (ignorando maiúsculas).",
        )

    def validar(self, senha):
        """Retorna os erros; uma lista vazia indica aprovação nas regras."""
        erros = []

        if not self.tamanho_minimo <= len(senha) <= self.tamanho_maximo:
            erros.append(f"A senha deve conter entre {self.tamanho_minimo} e {self.tamanho_maximo} caracteres.")
        if not any(caractere.isupper() for caractere in senha):
            erros.append("A senha deve conter pelo menos uma letra maiúscula.")
        if not any(caractere.islower() for caractere in senha):
            erros.append("A senha deve conter pelo menos uma letra minúscula.")
        if not any(caractere.isdigit() for caractere in senha):
            erros.append("A senha deve conter pelo menos um número.")
        if not any(caractere in self.caracteres_especiais for caractere in senha):
            erros.append("A senha deve conter pelo menos um caractere especial da lista.")
        if any(caractere.isspace() for caractere in senha):
            erros.append("A senha não deve conter espaços em branco.")
        if senha.lower() in self.senhas_bloqueadas:
            erros.append("A senha deve ser diferente de 'password', '12345678' e 'qwerty'.")

        return erros


def main():
    """Cria o objeto e conduz a interação pelo terminal."""
    validador = ValidadorSenha()
    print("Bem-vindo ao Validador de Senha!")
    print("Exercício didático: digite somente uma senha fictícia.")
    for numero, regra in enumerate(validador.obter_regras(), start=1):
        print(f"{numero}. {regra}")

    senha = input("Digite uma senha fictícia: ")
    erros = validador.validar(senha)
    if erros:
        print("Senha inválida pelas regras do exercício:")
        for erro in erros:
            print(f"- {erro}")
    else:
        print("Senha válida pelas regras do exercício!")


if __name__ == "__main__":
    main()
