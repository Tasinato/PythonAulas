"""Versão 1: fluxo sequencial de validação de senhas com regras de composição.

Use apenas entradas fictícias. A aprovação não mede a segurança real de uma senha.
"""

CARACTERES_ESPECIAIS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
SENHAS_BLOQUEADAS = {"password", "12345678", "qwerty"}
REGRAS = (
    "Conter entre 8 e 20 caracteres.",
    "Conter pelo menos uma letra maiúscula.",
    "Conter pelo menos uma letra minúscula.",
    "Conter pelo menos um número.",
    "Conter pelo menos um caractere especial da lista: " + CARACTERES_ESPECIAIS,
    "Não conter espaços em branco, tabulações ou quebras de linha.",
    "Ser diferente de 'password', '12345678' e 'qwerty' (ignorando maiúsculas).",
)


print("Bem-vindo ao Validador de Senha!")
print("Exercício didático: digite somente uma senha fictícia.")
for numero, regra in enumerate(REGRAS, start=1):
    print(f"{numero}. {regra}")

senha = input("Digite uma senha fictícia: ")

erros = []

if not 8 <= len(senha) <= 20:
    erros.append("A senha deve conter entre 8 e 20 caracteres.")
if not any(caractere.isupper() for caractere in senha):
    erros.append("A senha deve conter pelo menos uma letra maiúscula.")
if not any(caractere.islower() for caractere in senha):
    erros.append("A senha deve conter pelo menos uma letra minúscula.")
if not any(caractere.isdigit() for caractere in senha):
    erros.append("A senha deve conter pelo menos um número.")
if not any(caractere in CARACTERES_ESPECIAIS for caractere in senha):
    erros.append("A senha deve conter pelo menos um caractere especial da lista.")
if any(caractere.isspace() for caractere in senha):
    erros.append("A senha não deve conter espaços em branco.")
if senha.lower() in SENHAS_BLOQUEADAS:
    erros.append("A senha deve ser diferente de 'password', '12345678' e 'qwerty'.")


if erros:
    print("Senha inválida pelas regras do exercício:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("Senha válida pelas regras do exercício!")

