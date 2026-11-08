# PythonAulas

Material didático de Python organizado por **Rafael Tasinato** para comparar diferentes formas de organizar a solução de um mesmo problema.

## Atividades disponíveis

1. **Validador de senha em três abordagens** — comparação entre fluxo sequencial, funções e orientação a objetos, descrita abaixo.
2. **[Lista de exercícios: do básico ao intermediário](atividade_02_exercicios/README.md)** — dez questões com enunciados, resoluções, arquivos executáveis e exemplos para conferência.

## Uma atividade, três versões

O validador recebe uma senha fictícia e informa todas as regras não atendidas. Com a configuração padrão, as três versões aplicam **as mesmas regras e produzem as mesmas mensagens**.

| Arquivo | Abordagem | Objetivo didático |
| --- | --- | --- |
| [01_validador_sequencial.py](01_validador_sequencial.py) | Programação estruturada em um fluxo, sem funções próprias. | Praticar variáveis, condicionais e repetições. |
| [02_validador_com_funcoes.py](02_validador_com_funcoes.py) | Programação estruturada modularizada em funções. | Separar validação e interação, reutilizar a função e facilitar verificações. |
| [03_validador_orientado_a_objetos.py](03_validador_orientado_a_objetos.py) | Classe `ValidadorSenha`, com atributos e métodos. | Estudar classes, objetos, configuração e encapsulamento. |

**Funções não tornam um programa orientado a objetos.** A segunda versão continua estruturada; a terceira introduz uma classe que reúne configuração e comportamento. As três usam estruturas de sequência, seleção e repetição. Para um problema pequeno, a classe é uma alternativa didática, sem necessidade de herança ou outras camadas de complexidade.

## Regras comuns

- Entre 8 e 20 caracteres, inclusive.
- Pelo menos uma letra maiúscula, uma minúscula e um número.
- Pelo menos um caractere especial da lista exibida pelo programa.
- Nenhum espaço em branco, incluindo tabulações e quebras de linha.
- Ser diferente de `password`, `12345678` e `qwerty`, ignorando maiúsculas e minúsculas.

O exercício usa `isupper()`, `islower()`, `isdigit()` e `isspace()`, que reconhecem categorias Unicode; não restringe letras e números ao conjunto ASCII.

## Como executar

É necessário ter **Python 3** instalado. Não há dependências externas.

No diretório do projeto, escolha uma versão:

```bash
python 01_validador_sequencial.py
python 02_validador_com_funcoes.py
python 03_validador_orientado_a_objetos.py
```

Execute uma de cada vez. No Windows, pode utilizar `py` no lugar de `python`; em alguns sistemas, utilize `python3`.

## Exemplos de entradas fictícias

| Entrada | Resultado esperado nas três versões |
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

## Comparação para aula

| Questão | Sequencial | Com funções | Orientada a objetos |
| --- | --- | --- | --- |
| Onde ficam as regras? | Constantes e condições no fluxo principal. | Constantes e função `validar_senha`. | Atributos e métodos da classe `ValidadorSenha`. |
| Como executar a validação? | Executar o script. | Chamar `validar_senha(senha)`. | Criar um objeto e chamar `validador.validar(senha)`. |
| Como acessar os erros? | Lista `erros` no fluxo. | Lista retornada pela função. | Lista retornada pelo método. |
| O que ocorre na importação? | A interação começa, pois o código está no nível principal. | Não pede entrada: a interação fica em `main()`. | Não pede entrada: a interação fica em `main()`. |

Na versão com objetos, `ValidadorSenha(tamanho_minimo=10, tamanho_maximo=30)` exemplifica uma configuração diferente. A equivalência entre as três versões refere-se à configuração padrão de 8 a 20 caracteres.

## Atividades propostas

1. Executar as três versões com as mesmas entradas e comparar os resultados.
2. Identificar variáveis, condições, repetições, funções, classe, atributos e métodos.
3. Criar uma entrada que viole várias regras e explicar todas as mensagens.
4. Verificar os limites de 7, 8, 20 e 21 caracteres.
5. Alterar os limites de tamanho e comparar quais trechos precisam ser modificados em cada abordagem.
6. Explicar por que importar a versão sequencial inicia a interação e as outras duas não.

## Escopo didático

Use somente senhas fictícias. A entrada fica visível no terminal. A aprovação nas regras de composição não garante a segurança real de uma senha nem constitui um sistema de autenticação.


## Trajetória de aprendizado

O repositório público [Estudos-Python](https://github.com/Tasinato/Estudos-Python) preserva meus exercícios e anotações de cursos, incluindo os [estudos do curso de Luiz Otávio na Udemy](https://github.com/Tasinato/Estudos-Python/tree/main/Cursos/LuizOtavio-Udemy-Python3.0).

Aqui no PythonAulas, o foco é organizar atividades para estudo e ensino. Os exercícios antigos continuam no repositório de origem, com os créditos dos respectivos cursos e professores.
