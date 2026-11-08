def fatorial(n):
    """Calcula n! para um inteiro não negativo."""
    if n < 0:
        raise ValueError("Não é possível calcular o fatorial de um número negativo.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


if __name__ == "__main__":
    num = int(input("Digite um número para calcular o fatorial: "))
    if num < 0:
        print("Não é possível calcular o fatorial de um número negativo.")
    else:
        print(f"O fatorial de {num} é {fatorial(num)}")
