board_ = [
    ['C', 'A', 'T', 'F', 'Z', 'K', 'L'],
    ['B', 'G', 'E', 'S', 'E', 'A', 'U'],
    ['I', 'T', 'A', 'E', 'P', 'F', 'M'],
    ['S', 'E', 'A', 'T', 'N', 'Q', 'H'],
    ['T', 'F', 'Z', 'E', 'L', 'E', 'J'],
    ['A', 'I', 'W', 'O', 'D', 'J', 'A']
]


def find_first_symbol(board, word):
    # Поиск возможных позиций первой буквы слова на доске
    first_symbol = list(word)[0]
    finding_first_symbol = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == first_symbol:
                finding_first_symbol.append([i, j])
    # Возвращает список координат возможных позиций первой буквы слова
    return finding_first_symbol


def find_next_symbol(table_prev_symbols, num_symbol, board, word):
    # Поиск следующего возможного символа, используя список возможных позиций предыдущего символа
    # и его номер позиции в слове
    symbol = list(word)[num_symbol]
    symbol_position = []
    for key in table_prev_symbols:
        i = key[0]
        j = key[1]
        if j + 1 < len(board[i]):
            if board[i][j + 1] == symbol:
                symbol_position.append([i, j + 1])
        if i + 1 < len(board):
            if board[i + 1][j] == symbol:
                symbol_position.append([i + 1, j])
        if 0 <= j - 1:
            if board[i][j - 1] == symbol:
                symbol_position.append([i, j - 1])
        if 0 <= i - 1:
            if board[i-1][j] == symbol:
                symbol_position.append([i - 1, j])
    # Возвращает список возможных координат буквы из слова
    return symbol_position


def function(board, word):
    len_word = len(list(word))
    temp_list = find_first_symbol(board, word)
    if not temp_list:
        return False
    for num in range(1, len_word):
        temp_list = find_next_symbol(temp_list, num, board, word)
        if not temp_list:
            return False
    return True
