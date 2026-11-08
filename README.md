# PythonAulas

Material didático de Python organizado por **Rafael Tasinato**, com exercícios para praticar lógica de programação e organização de código.

## Atividade: validador de senha

O programa recebe uma entrada fictícia, verifica regras de composição e apresenta todas as regras não atendidas. O objetivo é estudar strings, funções, listas, estruturas condicionais e laços de repetição.

### Regras

- Entre 8 e 20 caracteres, inclusive.
- Pelo menos uma letra maiúscula, uma minúscula e um número.
- Pelo menos um caractere especial aceito pelo programa; a lista é exibida ao executar.
- Nenhum espaço em branco, incluindo tabulações e quebras de linha.
- Não utilizar `password`, `12345678` ou `qwerty`, ignorando maiúsculas e minúsculas.

## Como executar

É necessário ter **Python 3** instalado. O exercício utiliza somente a biblioteca padrão e não exige instalação de dependências.

No diretório do projeto, execute:

```bash
python validador_senha.py
```

No Windows, também é possível utilizar `py validador_senha.py`; em alguns sistemas, utilize `python3 validador_senha.py`.

## Exemplos de entradas fictícias

| Entrada | Resultado esperado |
| --- | --- |
| `Aula2026!` | Aprovada nas regras do exercício. |
| `aula2026!` | Falta uma letra maiúscula. |
| `AulaTeste!` | Falta um número. |
| `Aula2026` | Falta um caractere especial. |
| `Aula 2026!` | Contém espaço em branco. |

Exemplo de saída:

```text
Digite uma senha fictícia: aula2026!
Senha inválida pelas regras do exercício:
- A senha deve conter pelo menos uma letra maiúscula.
```

## Organização

- `validador_senha.py`: regras, função de validação e interação pelo terminal.
- `README.md`: objetivos, instruções e exemplos.

A função `validar_senha(senha)` retorna uma lista de mensagens de erro. Uma lista vazia indica aprovação nas regras. A interação fica em `main()`, permitindo importar a função sem iniciar a leitura de dados.

## Sugestões para aula

1. Explicar por que cada entrada da tabela é aceita ou rejeitada.
2. Criar novos exemplos que violem mais de uma regra.
3. Exercitar os limites de 8 e 20 caracteres.
4. Comparar a detecção de um espaço comum com outros espaços em branco.

## Escopo didático

Use somente senhas fictícias. A entrada fica visível no terminal. As regras de composição servem ao exercício e não garantem a segurança real de uma senha nem constituem um sistema de autenticação.
