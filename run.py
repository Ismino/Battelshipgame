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
    Placing ships and genereting a random position for them. Starting with a dictionary for the ships.
    """
   ships = {
    "battelship": "4",
    "aircraft_carrier": "4",
    "destroyer":"3",
    "gunboat":"2" 
   } 