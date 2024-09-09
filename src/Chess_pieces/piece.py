MAX_BOARD_SIZE = 8
MIN_BOARD_SIZE = 0

# constants -=-=-=-=-=-=-=-=-=-=-=-=-=-
CANT_MOVE = 0
CAN_MOVE = 1
CAN_KILL = 2

class chest_piece:
    """
    this is the parent class of all the chess pieces
    """
    def __init__(self, is_black: bool, ID: int) -> None:
        """this is the init function of all the chess pieces

        Args:
            is_black (bool): defines if the piece is black or white
            ID (int): id for the board to know where the piece is
        """
        self.is_black = is_black
        self.ID = ID
        
    def show_movement(self, board: list, x: int, y: int) -> dict:
        """this function will show the possible moves for the piece

        Args:
            board (list): the board of the game with all the pieces

        Returns:
            dict: list 8 on 8 of the possible moves, 0 is can't move, 1 is can move, 2 is can kill
        """
        pass