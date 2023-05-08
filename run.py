import random

def create_board():
    """
    Creating the board and making the bord the lenght of 6.
    """
    board = []
    for i in range(6):
        board.append([' '] * 6)
    return board

def print_board(board):
    """
    Printing the board
    """
    print("|" + "|".join(str(i) for i in range(1, 7)))
    for i, row in enumerate(board):
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

def main():
    board = create_board()
    print_board(board)
    ships = {'battleship': 4, 'cruiser': 3, 'destroyer': 2}
    ships_placement(board, ships)
    get_guess()

main()
