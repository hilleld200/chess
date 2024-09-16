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
    board[0][0] = rook.rook(True, "A1")
    board[0][1] = knight.knight(True, "B1")
    board[0][2] = bishop.bishop(True, "C1")
    board[0][3] = queen.queen(True, "D")
    board[0][4] = king.king(True, "E")
    board[0][5] = bishop.bishop(True, "C2")
    board[0][6] = knight.knight(True, "B2")
    board[0][7] = rook.rook(True, "A2")
    
    # white side
    board[7][0] = rook.rook(False, "a1")
    board[7][1] = knight.knight(False, "b1")
    board[7][2] = bishop.bishop(False, "c1")
    board[7][3] = queen.queen(False, "d")
    board[7][4] = king.king(False, "e")
    board[7][5] = bishop.bishop(False, "c2")
    board[7][6] = knight.knight(False, "b2")
    board[7][7] = rook.rook(False, "a2")
    
    # pawns
    for i in range(8):
        board[1][i] = pawn.pawn(True, "P " + str(i + 1))
        board[6][i] = pawn.pawn(False, "p " + str(i + 1))
    
    return board

