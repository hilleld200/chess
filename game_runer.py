from src.Chess_pieces import Board

# constants -=-=-=-=-=-=-=-=-=-=-=-=-=-
COLORS = {
    'black': '\033[30m',
    'white': '\033[37m',
    'blue': '\033[34m',
    'green': '\033[32m',
    'red': '\033[31m',
    1: '\033[33m',
    2: '\033[31m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

# custom exceptions -=-=-=-=-=-=-=-=-=-
class UserInputError(Exception):
    pass

# functions -=-=-=-=-=-=-=-=-=-=-=-=-=-
def print_board(board: list, movements: dict = {}) -> None:
    """this function will print the board with the movements

    Args:
        board (list): the game board
        movements (dict): the possible movements
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if (i, j) in movements:
                if board[i][j] is None:
                    print(f"{COLORS[movements[(i, j)]]}0{COLORS['reset']})", end=" ")
                else:
                    print(f"{COLORS[movements[(i, j)]]}{board[i][j].ID}{COLORS['reset']})", end=" ")
            else:
                print(0, end=" ")
        print()

def get_troop_positions(board: list, target_all: bool = False) -> tuple:
    """get from the user a position that have a troop

    Args:
        board (list): the game board
    
    Returns:
        tuple: (x, y)
    """
    print(COLORS['blue'], COLORS['bold'], end='')
    try:
        x = int(input("x: "))
        y = int(input("y: "))
    except ValueError:
        print(f"{COLORS['red']} enter a NUMBER {COLORS['reset']}")
        return get_troop_positions(board)
    print(COLORS['reset'], end='')
    
    if x < 1 or x > len(board[0]) or y < 1 or y > len(board):
        raise UserInputError("the number need to be between 1 and 8,\n e.g. (1, 1)\n\t you enter: ({}, {})".format(x, y))
    
    if board[x - 1][y - 1] is None or target_all:
        raise UserInputError(f"the position ({x}, {y}) is empty\n you need to enter a position that have troop")
    
    return x - 1, y - 1

def game_loop(board: list) -> bool:
    """this is the game loop that all the actions will be done

    Args:
        board (list): the board to be played on

    Returns:
        bool: if the black wins
    """
    black_turn = False
    
    
    while True:
        troop_x, troop_y, target_x, target_y = -1
        
        # get the target position
        print(COLORS['blue'], end='')
        if black_turn:
            print("black turn")
        else:
            print("white turn")
        print(COLORS['reset'], end='')
        
        try:
            troop_x, troop_y = get_troop_positions(board)
        except UserInputError as e:
            print(f"{COLORS['red']}{e}{COLORS['reset']}")
            continue
        
        # show the possible movements to the user
        selected_troop = board[troop_x][troop_y]
        possible_movements: dict = selected_troop.show_movement(board, troop_x, troop_y)
        
        print_board(board, possible_movements)
        while target_x == -1:
            try:
                target_x, target_y = get_troop_positions(board, True)
            except UserInputError as e:
                print(f"{COLORS['red']}{e}{COLORS['reset']}")
                continue
            
        if type(board[target_x][target_y]).__name__ == 'king':
            return black_turn 
        board[target_x][target_y] = selected_troop
        board[troop_x][troop_y] = None
        
        
        black_turn = not black_turn
            



# main -=-=-=-=-=-=-=-=-=-=-=-=-=-
def main():
    user_option = 0
    while user_option != 2:
        user_option = int(input(f"1. {COLORS['blue']}Start Game\n{COLORS['reset']}2. {COLORS['red']}Exit{COLORS['reset']}\n"))
        if user_option == 1:
            game_board = Board.init_board()
            print("the board is ready")
            print_board(game_board)
            black_win = game_loop(game_board)



if __name__ == "__main__":
    main()
