import math

# Define the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check for a draw
def check_draw(board):
    return ' ' not in board

# Function to make a move
def make_move(board, position, player):
    board[position] = player

# Function to get available moves
def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

# Main function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        make_move(board, move, 'X')

        # Check for win or draw
        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = get_best_move(board, 'O')
        make_move(board, ai_move, 'O')

        # Check for win or draw
        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

# Function to implement the Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to get the best move for the AI
def get_best_move(board, player):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = player
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

if __name__ == "__main__":
    play_game()
