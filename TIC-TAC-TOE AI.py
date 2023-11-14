
import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return -1 if maximizing_player else 1

    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row, col = map(int, input("Enter your move (row and column, space-separated): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'O'

        if check_winner(board):
            print_board(board)
            print("AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play()

