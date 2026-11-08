def is_palindromo(texto):
    """Ignora maiúsculas e espaços comuns; preserva acentos e pontuação."""
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


if __name__ == "__main__":
    palavra = input("Digite uma palavra ou frase: ")
    if is_palindromo(palavra):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
