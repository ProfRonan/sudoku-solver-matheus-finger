"""Main module to run the program."""

import copy

def is_valid_mais_rapido(board: list[list[int]], linha: int, coluna:int) -> bool: 
    """Checa se a jogada é válida"""
    # checando linha
    if not checa_setor(board[linha]):
        return False
    # criando lista com coluna
    col = []
    for i in range (0, 9):
        col.append(board[i][coluna])
    # checando coluna
    if not checa_setor(col):
        return False
    # checando começo do setor
    if linha < 3:
        comeco_linha = 0
    elif linha < 6:
        comeco_linha = 3
    else:
        comeco_linha = 6
    if coluna < 3:
        comeco_coluna = 0
    elif coluna < 6:
        comeco_coluna = 3
    else:
        comeco_coluna = 6
    # checando setor
    if not checa_setor(faz_quadrado(board, comeco_linha, comeco_coluna)):
        return False
    return True

def testa_possibilidades(board) -> dict[list[int]]:
    """
    Cria uma dicionário de possibilidades onde a chave é a coordenada,
     e o valor são as possibilidades de números
    """
    novo_board = copy.deepcopy(board)
    dicio_possibilidades_testa = {}
    # Percorre tabuleiro
    for i in range(0, 9):
        for j in range(0,9):
            # Se a célula estiver vazia, calcula as possibilidades
            if novo_board[i][j] == 0:
                possibilidades = []
                # As possibilidades vão dos números 1 a 9
                for teste in range(1, 10):
                    # Altera o tabuleiro para fazer o teste
                    novo_board[i][j] = teste
                    # Se retornar como válido, adiciona o teste nas possibilidades
                    if is_valid_mais_rapido(novo_board, i, j):
                        possibilidades.append(teste)
                novo_board[i][j] = 0
                # Adiciona as coordenadas da célula e suas possibilidades no dcionário
                if len(possibilidades) > 0:
                    dicio_possibilidades_testa[(i, j)] = possibilidades
    # se tiveram elementos no dicionário, organizar pela quantidade de possibilidades
    if len(dicio_possibilidades_testa) > 0:
        minhasChavesOrganizadas = sorted(dicio_possibilidades_testa, key=lambda k: len(dicio_possibilidades_testa[k]))
        dicio_organizado = {indice : dicio_possibilidades_testa[indice] for indice in minhasChavesOrganizadas}
        return dicio_organizado
    return dicio_possibilidades_testa

def nao_tem_mais_zero(board) -> bool:
    """
    Verifica se ainda há 0 no tabuleiro.
    """
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return False
    return True

def recursao(board, dicio_possibilidades):
    """
    Percorre o dicionário de possibilidades, altera a posição
    com menor número de possibilidades e recalcula as possibilidades,
    depois chama ela mesma para continuar o percurso.
    Caso a lista de possibilidades fique vazia, há duas opções:
    1. Ele concluiu o tabuleiro, pois todos os números estão preenchidos.
    E então, retorna o tabuleiro.
    2. Ele chegou em um beco sem saída e deve continuar percorrendo as outras
    possibilidades.
    """
    # percorre o dicionário com as possibilidades
    for coordenadas in dicio_possibilidades:
        # percorre as listas de possibilidades para cada posição
        for teste in dicio_possibilidades[coordenadas]:
            # faz uma cópia do tabuleiro que é modificável sem
            # alterar o arquivo original que lhe foi passado
            novo_board = copy.deepcopy(board)
            # atribui uma das possibilidades para a coordenada
            # da lista que ele está percorrendo
            novo_board[coordenadas[0]][coordenadas[1]] = teste
            # recalcula as possibilidades
            novo_dicio_possibilidades = testa_possibilidades(novo_board)
            # verificando se não há mais possibilidades
            if len(novo_dicio_possibilidades) == 0:
                # se não há mais possibilidades e não há mais zeros na borda
                # então ele concluiu o sudoku
                if nao_tem_mais_zero(novo_board):
                    return novo_board
                # caso ainda exista 0 no tabuleiro, então o programa
                # só continua percorrendo as possibilidades
            else:
                # se ainda há possibilidades, ele vai então
                # chamar a mesma função com a modificação aplicada
                # para checar se ele vai retornar o tabuleiro (caso
                # ache a solução) ou simplesmente não vai retornar
                # nada e então o for continua percorrendo as outras
                # possibilidades
                result = recursao(novo_board, novo_dicio_possibilidades)
                # se a função retornar um tabuleiro, então ele retorna
                # o tabuleiro
                if result != None:
                    return result

def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    # Calcula as possibilidades inicias
    dicio_possibilidades = testa_possibilidades(board)
    # utiliza método recursão que retorna o tabuleiro feito
    return recursao(board, dicio_possibilidades)

def checa_setor(setor: list[int]):
    """
    Verifica se há números repetidos em uma lista,
    tirando os números 0 (célula vazia)
    """
    for i in range(0, len(setor)):
        for j in range(i+1, len(setor)):
            if setor[i] != 0 and setor[i] == setor[j]:
                return False
    return True

def faz_quadrado(board: list[list[int]], linha_inicio: int, coluna_inicio: int) -> list[int]:
    """
    Faz um setor quadrado a partir de coordenadas do inicio
    e final da linha
    """
    quadrado = []
    for i in range(linha_inicio, linha_inicio+3):
        for j in range(coluna_inicio, coluna_inicio+3):
            quadrado.append(board[i][j])
    return quadrado

def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    if len(board) != 9:
        return False
    for i in range(0, 9):
        if len(board[i]) != 9:
            return False
        coluna = []
        for j in range (0, 9):
            coluna.append(board[j][i])
            if type(board[i][j]) is not int:
                return False
            elif board[i][j] > 9 or board[i][j] < 0:
                return False
        if not checa_setor(board[i]):
            return False
        if not checa_setor(coluna):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not checa_setor(faz_quadrado(board, i, j)):
                return False

    return True