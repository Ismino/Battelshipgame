import random

def create_board():
    """
    Creating the board and making the bord the lenght of 6.
    """
    board = []
    for i in range(6):
        board.append([' '] * 6)
    return board

board = create_board()
print(board)

def ships(board):
    """
    Placing ships and genereting a random position for them. Starting with a dictionary for the ships and then randomly place them.
    """
   ships = {
    "battelship": "4",
    "aircraft_carrier": "4",
    "destroyer":"3",
    "gunboat":"2" 
   } 
    for ship in ships:
        onboard = False
        while not onboard:
            x = random.randint(0,5)
            y = random.randint(0,5)
            aligntment = random.choice(['horizontal','vertical'])
            if aligntment == 'horizontal' and y ships[ship] <= 6:
                valid_placement = True
                for i in range(ships[ship]):
                    if board[x][y+i] != ' ':
                        valid_placement = False
                        break
                if valid_placement:
                    for i in range(ships[ship]):
                        board [x][y+i]= ship[0].upper()
                    onboard = True    
            elif aligntment == 'vertical' and x ships[ship] <= 6:
                valid_placement = True 
                for i in range(ships[ship]):
                    if board[x+i][y] != ' ':
                        valid = False
                        break
                if valid:
                    for i in range(ships[ship]):
                        board[x+i][y] = ship[0].upper()
                    placed = True


