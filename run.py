import random

def create_board():
    """
    Creating the board and making the bord the lenght of 6.
    """
    board = []
    for i in range(6):
        board.append([' '] * 6)
    return board

def print_board(board, hide_ships=True):
    """
    Printing the board. If hide_ships is True, ship locations are hidden.
    """
    print("|" + "|".join(str(i) for i in range(1, 7)))
    for i, row in enumerate(board):
        if hide_ships:
            # Replace ship characters with spaces
            row = [' ' if cell in ['B', 'C', 'D'] else cell for cell in row]
        print(str(i + 1) + "|" + "|".join(row) + "|")

def ships_placement(board, ships):
    """
    Placing ships and genereting a random position for them. Starting with a dictionary for the ships and then randomly place them.
    """
    for ship in ships:
        onboard = False
        while not onboard:
            x = random.randint(0,5)
            y = random.randint(0,5)
            aligntment = random.choice(['horizontal','vertical'])
            if aligntment == 'horizontal' and y + ships[ship] <= 6:
                valid_placement = True
                for i in range(ships[ship]):
                    if board[x][y+i] != ' ':
                        valid_placement = False
                        break
                if valid_placement:
                    for i in range(ships[ship]):
                        board [x][y+i]= ship[0].upper()
                    onboard = True    
            elif aligntment == 'vertical' and x + ships[ship] <= 6:
                valid_placement = True 
                for i in range(ships[ship]):
                    if board[x+i][y] != ' ':
                        valid = False
                        break
                if valid_placement:
                    for i in range(ships[ship]):
                        board[x+i][y] = ship[0].upper()
                    onboard = True
def get_guess():
    """
    Getting the guess from the user and returning as a tuple.
    """
    while True:
        try:
            guess = input("Enter your guess (row,column): ")
            row, col = guess.split(",")
            row = int(row)
            col = int(col)
            if row < 1 or row > 6 or col < 1 or col > 6:
                print("Invalid input. Please enter values between 1 and 6.")
            else:
                return (row, col) 
        except ValueError:
            print("Invalid input. Please enter values in the format 'row,column'.") 
def check_guess(guess, board):
    """
    Checks the users guesses and prints out hit or miss for misses and hits.
    """
    row, col = guess
    if board[row-1][col-1] != ' ':
        board[row-1][col-1] = 'X'
        print("Hit!")
        return True
    else:
        board[row-1][col-1] = 'O'
        print("Miss!")
        return False

def play_battleship():
    """
    Calls the previus made functions and makes the game 15 rounds long, also prints out some messeges.
    """
    board = create_board()
    ships = {'battleship': 4, 'cruiser': 3, 'destroyer': 2}
    ships_placement(board, ships)
    print("Let's play Battleship!")
    for i in range(15):
        print("Round", i+1)
        print_board(board, hide_ships=True)
        guess = get_guess()
        check_guess(guess, board)
    print("Game over!")
    
play_battleship()