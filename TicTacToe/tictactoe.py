import math

board = [" " for _ in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game loop
while True:
    print_board()
    
    # Player move
    user = int(input("Enter position (0-8): "))
    if board[user] != " ":
        print("Invalid move!")
        continue
    board[user] = "X"

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    # AI move
    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break
