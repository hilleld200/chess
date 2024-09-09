# board.py
from src.Chess_pieces import bishop, king, knight, pawn, queen, rook
# size of the board
MAX_BOARD_SIZE = 8
MIN_BOARD_SIZE = 0

def init_board() -> list:
    """this function creates the board and add all the pieces

    Returns:
        list: the board with all the pieces
    """
    board = [[None for _ in range(MAX_BOARD_SIZE)] for _ in range(MAX_BOARD_SIZE)]
    # black side
    board[0][0] = rook.rook(True, 1)
    board[0][1] = knight.knight(True, 2)
    board[0][2] = bishop.bishop(True, 3)
    board[0][3] = queen.queen(True, 4)
    board[0][4] = king.king(True, 5)
    board[0][5] = bishop.bishop(True, 6)
    board[0][6] = knight.knight(True, 7)
    board[0][7] = rook.rook(True, 8)
    
    # white side
    board[7][0] = rook.rook(False, 109)
    board[7][1] = knight.knight(False, 110)
    board[7][2] = bishop.bishop(False, 111)
    board[7][3] = queen.queen(False, 112)
    board[7][4] = king.king(False, 113)
    board[7][5] = bishop.bishop(False, 114)
    board[7][6] = knight.knight(False, 115)
    board[7][7] = rook.rook(False, 116)
    
    # pawns
    for i in range(8):
        board[1][i] = pawn.pawn(True, i + 1)
        board[6][i] = pawn.pawn(False, i + 100)
    
    return board

