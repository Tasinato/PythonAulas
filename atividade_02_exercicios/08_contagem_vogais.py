def contar_vogais(texto):
    """Conta vogais sem acento, em maiúsculas ou minúsculas."""
    vogais = "aeiouAEIOU"
    contagem = 0
    for caractere in texto:
        if caractere in vogais:
            contagem += 1
    return contagem


if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    print(f"O número de vogais na frase é: {contar_vogais(frase)}")
