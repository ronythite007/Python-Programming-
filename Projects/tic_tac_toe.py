import math

# Initialize the board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for a winner
def check_winner(board, player):
    win_cond = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_cond

# Check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Get empty positions
def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizingPlayer):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0
    
    if maximizingPlayer:
        maxEval = -math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Find the best move
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for (i, j) in get_empty_positions(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, -math.inf, math.inf, False)
        board[i][j] = ' '
        if move_val > best_val:
            move = (i, j)
            best_val = move_val
    return move

# Main game loop
def play_game():
    board = create_board()
    human_turn = True

    while True:
        print_board(board)
        
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        
        if human_turn:
            print("Your turn! Enter row and column (0, 1, or 2):")
            row, col = map(int, input().split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                human_turn = False
            else:
                print("Invalid move! Try again.")
        else:
            print("AI's turn:")
            row, col = best_move(board)
            board[row][col] = 'O'
            human_turn = True

# Start the game
play_game()

