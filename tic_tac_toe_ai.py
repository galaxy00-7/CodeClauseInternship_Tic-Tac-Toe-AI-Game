import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move! Enter a number from 1 to 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try another.")
        except ValueError:
            print("Please enter a valid number.")

def get_ai_move(board):
    # Random AI move
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human
    ai_player = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = get_user_move(board)
        else:
            row, col = get_ai_move(board)
            print(f"AI chose: {row * 3 + col + 1}")

        board[row][col] = current_player
        print_board(board)

        if is_winner(board, current_player):
            if current_player == "X":
                print("🎉 You win!")
            else:
                print("💻 AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()