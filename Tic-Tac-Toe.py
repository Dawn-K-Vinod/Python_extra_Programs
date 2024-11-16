# Initialize global variables for the board
R11 = R12 = R13 = R21 = R22 = R23 = R31 = R32 = R33 = None

def insert(X_or_O, x):
    """Insert X or O into the correct board position based on x."""
    global R11, R12, R13, R21, R22, R23, R31, R32, R33
    if x == '11':
        R11 = X_or_O
    elif x == '12':
        R12 = X_or_O
    elif x == '13':
        R13 = X_or_O
    elif x == '21':
        R21 = X_or_O
    elif x == '22':
        R22 = X_or_O
    elif x == '23':
        R23 = X_or_O
    elif x == '31':
        R31 = X_or_O
    elif x == '32':
        R32 = X_or_O
    elif x == '33':
        R33 = X_or_O

def check(X_or_O):
    """Check if the given player has won."""
    if (R11 == R12 == R13 == X_or_O or  # Rows
        R21 == R22 == R23 == X_or_O or
        R31 == R32 == R33 == X_or_O or
        R11 == R21 == R31 == X_or_O or  # Columns
        R12 == R22 == R32 == X_or_O or
        R13 == R23 == R33 == X_or_O or
        R11 == R22 == R33 == X_or_O or  # Diagonals
        R13 == R22 == R31 == X_or_O):
        print(f"Player {'1' if X_or_O == 'X' else '2'} won!")
        return True
    return False

def print_board():
    """Display the current board."""
    global R11, R12, R13, R21, R22, R23, R31, R32, R33
    board = [
        [R11 or " ", R12 or " ", R13 or " "],
        [R21 or " ", R22 or " ", R23 or " "],
        [R31 or " ", R32 or " ", R33 or " "],
    ]
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def tic_tac_toe():
    """Main game loop."""
    input_numbers = ['1', '2', '3']
    lst1 = []  # List to track already inserted positions

    for i in range(9):  # Total 9 moves max
        player = 1 if i % 2 == 0 else 2
        X_or_O = 'X' if player == 1 else 'O'

        while True:
            print("\nCurrent Board Position")
            print_board()
            print(f"** Player {player}'s Turn **")
            row = input("Enter the row (1-3): ")
            col = input("Enter the column (1-3): ")

            if row in input_numbers and col in input_numbers:
                x = row + col
                if x in lst1:
                    print("Already inserted! Try again.")
                    continue
                break
            else:
                print("Invalid Entry! Try again.")

        lst1.append(x)
        insert(X_or_O, x)

        if i >= 4:  # Minimum moves required to win
            if check(X_or_O):
                print_board()
                return

    print_board()
    print("It's a tie!\n#Game Over#")

# Start the game
tic_tac_toe()