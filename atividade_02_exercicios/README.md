# Atividade 02 — Lista de exercícios de programação em Python

## Do básico ao intermediário

Esta atividade tem como objetivo testar e aprimorar conhecimentos em Python, com exercícios de entrada e saída, condicionais, repetição, funções, strings e listas. Cada questão inclui uma resolução para conferir seu entendimento.

**Como estudar:** tente resolver cada questão antes de abrir a resolução. Depois, compare sua solução com o exemplo e execute outras entradas.

## Como executar

Requisito: **Python 3**, sem dependências externas. A partir da raiz do repositório, execute, por exemplo:

```bash
python atividade_02_exercicios/01_ola_mundo.py
python atividade_02_exercicios/10_calculadora.py
```

Escolha um arquivo de cada vez. No Windows, pode usar `py`; em outros sistemas, `python3`. Os exercícios numéricos pressupõem entradas válidas: inteiros quando solicitado e ponto como separador decimal na calculadora.

## Questões

### 1. Olá, Mundo!

**Questão:** Escreva um programa que imprima "Olá, Mundo!" na tela.

**Conceitos:** Saída de dados com print.

[Arquivo executável: 01_ola_mundo.py](01_ola_mundo.py)

<details>
<summary>Ver resolução</summary>

```python
print("Olá, Mundo!")
```

</details>

### 2. Soma de dois números

**Questão:** Peça ao usuário dois números inteiros e imprima a soma deles.

**Conceitos:** Entrada de dados, conversão para int e operadores aritméticos.

[Arquivo executável: 02_soma.py](02_soma.py)

<details>
<summary>Ver resolução</summary>

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)
```

</details>

### 3. Par ou ímpar

**Questão:** Peça ao usuário um número inteiro e determine se ele é par ou ímpar.

**Conceitos:** Condicionais e operador de resto %.

[Arquivo executável: 03_par_ou_impar.py](03_par_ou_impar.py)

<details>
<summary>Ver resolução</summary>

```python
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

</details>

### 4. Maior de três números

**Questão:** Peça ao usuário três números inteiros e imprima o maior deles.

**Conceitos:** Comparações, operadores lógicos e if/elif/else.

[Arquivo executável: 04_maior_de_tres.py](04_maior_de_tres.py)

<details>
<summary>Ver resolução</summary>

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)
```

</details>

### 5. Tabuada

**Questão:** Peça ao usuário um número inteiro e imprima a tabuada desse número de 1 a 10.

**Conceitos:** Laços for, range e f-strings.

[Arquivo executável: 05_tabuada.py](05_tabuada.py)

<details>
<summary>Ver resolução</summary>

```python
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

</details>

### 6. Fatorial

**Questão:** Escreva uma função que calcule o fatorial de um número inteiro não negativo, incluindo 0! = 1.

**Conceitos:** Funções, acumuladores, repetição e validação do domínio.

[Arquivo executável: 06_fatorial.py](06_fatorial.py)

<details>
<summary>Ver resolução</summary>

```python
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
```

</details>

### 7. Verificador de palíndromo

**Questão:** Escreva uma função que verifique se uma palavra ou frase é um palíndromo, ignorando maiúsculas e espaços comuns.

**Conceitos:** Funções, métodos de strings e fatiamento.

[Arquivo executável: 07_palindromo.py](07_palindromo.py)

<details>
<summary>Ver resolução</summary>

```python
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
```

</details>

### 8. Contagem de vogais

**Questão:** Escreva uma função que conte as vogais a, e, i, o, u em uma string, incluindo maiúsculas.

**Conceitos:** Funções, iteração sobre strings e contadores.

[Arquivo executável: 08_contagem_vogais.py](08_contagem_vogais.py)

<details>
<summary>Ver resolução</summary>

```python
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
```

</details>

### 9. Lista ordenada

**Questão:** Dada a lista de números inteiros [5, 2, 8, 1, 9, 4], ordene-a em ordem crescente.

**Conceitos:** Listas e ordenação com sort.

[Arquivo executável: 09_lista_ordenada.py](09_lista_ordenada.py)

<details>
<summary>Ver resolução</summary>

```python
lista_numeros = [5, 2, 8, 1, 9, 4]
lista_numeros.sort()
print("Lista ordenada:", lista_numeros)
```

</details>

### 10. Calculadora simples

**Questão:** Crie uma calculadora para adição, subtração, multiplicação e divisão entre dois números. Trate divisão por zero e operador inválido.

**Conceitos:** Funções, números reais e condicionais aninhadas.

[Arquivo executável: 10_calculadora.py](10_calculadora.py)

<details>
<summary>Ver resolução</summary>

```python
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
```

</details>

## Exemplos para conferência

| Exercício | Entrada ou situação | Resultado esperado |
| --- | --- | --- |
| Olá, Mundo! | Sem entrada. | `Olá, Mundo!` |
| Soma | `7` e `-2`. | `A soma é: 5` |
| Par ou ímpar | `0`; depois `-3`. | Par; ímpar. |
| Maior de três | `4`, `9`, `9`. | `O maior número é: 9` |
| Tabuada | `3`. | Dez linhas, de `3 x 1 = 3` a `3 x 10 = 30`. |
| Fatorial | `0`; `5`; `-1`. | `1`; `120`; mensagem sobre número negativo. |
| Palíndromo | `A sacada da casa`; `Python`. | É palíndromo; não é palíndromo. |
| Vogais | `Python e legal`. | `4` vogais. |
| Ordenação | Lista fornecida. | `[1, 2, 4, 5, 8, 9]` |
| Calculadora | `8`, `/`, `2`; depois divisor `0`. | `4.0`; mensagem de divisão por zero. |

## Observações didáticas

- As resoluções são exemplos possíveis, não as únicas soluções corretas.
- O fatorial inclui zero e rejeita números negativos.
- O palíndromo ignora apenas maiúsculas/minúsculas e espaços comuns. Acentos, pontuação e outros espaços são preservados; a entrada vazia é considerada palíndromo por essa implementação.
- A contagem de vogais considera somente `a`, `e`, `i`, `o`, `u` e suas maiúsculas, conforme a proposta original. Vogais acentuadas podem ser uma extensão da atividade.
- `sort()` modifica a lista original; compare seu comportamento com `sorted()` como exercício adicional.
- As funções dos exercícios 6, 7, 8 e 10 podem ser importadas sem iniciar a interação. Os demais arquivos são exemplos de fluxo sequencial.

## Desafios de continuidade

1. Tratar entradas numéricas inválidas com `try/except`.
2. Repetir a calculadora até o usuário escolher sair.
3. Adaptar o palíndromo para ignorar pontuação e discutir como tratar acentos.
4. Contar vogais acentuadas e comparar os resultados.
5. Reorganizar um exercício sequencial em funções e explicar o que mudou.

[Voltar ao README principal](../README.md)
