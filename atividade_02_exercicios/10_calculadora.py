def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    if operador == "+":
        print(f"Resultado: {num1 + num2}")
    elif operador == "-":
        print(f"Resultado: {num1 - num2}")
    elif operador == "*":
        print(f"Resultado: {num1 * num2}")
    elif operador == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operador inválido.")


if __name__ == "__main__":
    calculadora()
