# Python Sudoku Solver

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Nesse script, voce irá implementar duas funções que resolvem um tabuleiro de [Sudoku](https://pt.wikipedia.org/wiki/Sudoku) na versão 9x9.

A função `solve_sudoku` recebe um tabuleiro de Sudoku incompleto e retorna o tabuleiro completo.
Caso seja impossível completar o tabuleiro passado, a função deve lançar uma exceção do tipo `ValueError` com a mensagem `Sudoku impossível de resolver`.

A função `is_valid` recebe um tabuleiro de Sudoku e verifica se ele é válido retornando `False` caso ele seja inválido e `True` quando ele é válido.
Um tabuleiro de Sudoku é válido se ele não viola nenhuma das regras do jogo.

As regras são as seguintes:

1. Cada linha deve conter os números de 1 a 9 sem repetição.
2. Cada coluna deve conter os números de 1 a 9 sem repetição.
3. Temos 9 subgrid 3x3 que devem conter os números de 1 a 9 sem repetição.
4. Cada célula deve conter um número de 1 a 9 ou estar vazia.

Para facilitar a implementação, assuma que `0` em uma célula representa uma célula vazia.
Também, assuma que o tabuleiro de Sudoku é uma lista de listas de inteiros.
Ou seja, um tabuleiro de Sudoku é uma lista de 9 listas de 9 inteiros.

Um exemplo de Sudoku válido, mas ainda incompleto, é o seguinte:

```python
sudoku_board = [
   [5, 3, 0, 0, 7, 0, 0, 0, 0],
   [6, 0, 0, 1, 9, 5, 0, 0, 0],
   [0, 9, 8, 0, 0, 0, 0, 6, 0],
   [8, 0, 0, 0, 6, 0, 0, 0, 3],
   [4, 0, 0, 8, 0, 3, 0, 0, 1],
   [7, 0, 0, 0, 2, 0, 0, 0, 6],
   [0, 6, 0, 0, 0, 0, 2, 8, 0],
   [0, 0, 0, 4, 1, 9, 0, 0, 5],
   [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

## 🧑‍💻 Exemplo de Execução 🧑‍💻

```python
>>> sudoku_board = [
   [5, 3, 0, 0, 7, 0, 0, 0, 0],
   [6, 0, 0, 1, 9, 5, 0, 0, 0],
   [0, 9, 8, 0, 0, 0, 0, 6, 0],
   [8, 0, 0, 0, 6, 0, 0, 0, 3],
   [4, 0, 0, 8, 0, 3, 0, 0, 1],
   [7, 0, 0, 0, 2, 0, 0, 0, 6],
   [0, 6, 0, 0, 0, 0, 2, 8, 0],
   [0, 0, 0, 4, 1, 9, 0, 0, 5],
   [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
>>> is_valid(sudoku_board)
True
>>> solved_board = solve_sudoku(sudoku_board)
>>> is_valid(solved_board)
True
>>> solved_board
[
   [5, 3, 4, 6, 7, 8, 9, 1, 2],
   [6, 7, 2, 1, 9, 5, 3, 4, 8],
   [1, 9, 8, 3, 4, 2, 5, 6, 7],
   [8, 5, 9, 7, 6, 1, 4, 2, 3],
   [4, 2, 6, 8, 5, 3, 7, 9, 1],
   [7, 1, 3, 9, 2, 4, 8, 5, 6],
   [9, 6, 1, 5, 3, 7, 2, 8, 4],
   [2, 8, 7, 4, 1, 9, 6, 3, 5],
   [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
```

## 🧪 Testes Automáticos 🧪

Para testar automaticamente o programa **antes** de fazer um commit e enviar o seu trabalho existem algumas formas de fazer isso.

1. executar o módulo `unittest` direto no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python -m unittest discover -s test
```

2. executar o arquivo `test_main.py` no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python test/test_main.py
```

3. caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.

4. no seu editor de código, você pode executar o arquivo `test_main.py` e verificar o resultado dos testes no terminal.

## 👋 Envio do Trabalho 👋

Para enviar o seu trabalho, basta fazer um **commit** e um **push** para o repositório do exercício.

No terminal, você pode fazer isso executando os seguintes comandos:

```bash
git add .
git commit -m "Entrega do exercício"
git push
```

No [VSCode](https://code.visualstudio.com/), você pode fazer isso apertando `CTRL+SHIFT+G` para abrir o menu de controle de versão e utilizar a interface gráfica para fazer o **commit** e o **push/sync**.

## 🤖 Observações Importantes 🤖

- **Não altere o nome dos arquivos**. Os arquivos `test_main.py` e `main.py` precisam ter esses nomes para que os testes funcionem.
- **Não altere o nome das funções**. Os testes dependem que as funções tenham os nomes especificados no enunciado ou já escritos nos arquivos.
- **Não altere o nome dos parâmetros**. Os testes dependem que as funções tenham os parâmetros especificados no enunciado ou já escritos nos arquivos.
- **Antes de fazer um commit**, execute os testes usando um dos métodos acima para verificar se o seu programa está funcionando corretamente.
- **Caso não consiga corrigir os erros**, entre em contato com o professor ou monitores para que eles possam te ajudar.
  Para isso você deve fazer um commit com o seu trabalho incompleto e abrir uma **issue** no repositório do exercício explicando o seu problema.

## 👀 Curiosidades 👀

O arquivo `requirements.txt` contém uma lista de dependências que o seu programa precisa para funcionar.

No caso desse exercício, a única dependência é o módulo `unittest` que é usado para fazer os testes automáticos.
E como o módulo `unittest` já vem instalado com o python, não é necessário instalar nada.

> Quando precisarmos instalar dependências, o comando `pip` é usado para instalar pacotes do python.
> Caso você precise instalar as dependências do seu programa, basta executar o seguinte comando:
>
> ```bash
> pip install -r requirements.txt
> ```

Os arquivos `Dockerfile` contém as instruções para criar uma imagem do docker com o seu programa.
Isso é útil para que eu possa executar o seu programa em um ambiente controlado e não ter problemas com dependências nem com possível códigos maliciosos na hora de rodar o programa.
São usados dois arquivos `Dockerfile`, um para rodar o seu programa e outro para rodar os testes.

Os arquivos dentro `.vscode` servem para configurar o ambiente de desenvolvimento no [VSCode](https://code.visualstudio.com/).
E facilitar a execução dos testes e do programa.

Os arquivos dentro da pasta `test` são usados para testar o seu programa.

O arquivo `.gitignore` serve para dizer ao git quais arquivos ele deve ignorar.

### :whale: Rodando o programa dentro do docker :whale:

Para aqueles que gostariam de aprender mais sobre o [docker](https://www.docker.com/), aqui vai uma breve explicação de como usar o docker para rodar o seu programa e os testes.

Primeiro, você precisa instalar o docker na sua máquina.
Para isso, basta seguir as instruções do site do [docker](https://docs.docker.com/get-docker/).

Depois de instalar o docker, você precisa criar uma imagem do docker com o seu programa.
Para isso, você precisa criar um arquivo `Dockerfile` com as instruções para criar a imagem do docker.
No caso desse exercício, o arquivo `Dockerfile` já está pronto.

Para criar a imagem do docker com o seu programa, basta executar o seguinte comando:

```bash
docker build -t python-app .
```

Para rodar o seu programa dentro do docker, basta executar o seguinte comando:

```bash
docker run -it --rm python-app
```

Para criar a imagem do docker com os testes, basta executar o seguinte comando:

```bash
docker build -t python-app-test -f test/Dockerfile .
```

Para rodar os testes dentro do docker, basta executar o seguinte comando:

```bash
docker run -it --rm python-app-test
```
