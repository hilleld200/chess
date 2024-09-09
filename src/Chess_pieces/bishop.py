import src.Chess_pieces.piece as piece

class bishop(piece.chest_piece):
    
    def show_movement(self, board: list, x: int, y: int) -> dict:
        i: int = 1
        possibles_moves: dict = {}
        checks = []
        
        # check for the down-right side
        while x + i < piece.MAX_BOARD_SIZE and y + i < piece.MAX_BOARD_SIZE:
            checks.append((x + i, y + i))
            if board[x + i][y + i] != None:
                break
            i += 1
            
        i = 1
        # check for the down-left side
        while x - i >= piece.MIN_BOARD_SIZE and y + i < piece.MAX_BOARD_SIZE:
            checks.append((x - i, y + i))
            if board[x - i][y + i] != None:
                break
            i += 1
            
        i = 1
        # check for the up-right side
        while x + i < piece.MAX_BOARD_SIZE and y - i >= piece.MIN_BOARD_SIZE:
            checks.append((x + i, y - i))
            if board[x + i][y - i] != None:
                break
            i += 1
            
        i = 1
        # check for the up-left side
        while x - i >= piece.MIN_BOARD_SIZE and y - i >= piece.MIN_BOARD_SIZE:
            checks.append((x - i, y - i))
            if board[x - i][y - i] != None:
                break
            i += 1
            
        for i, j in checks:
            if board[i][j] == None:
                possibles_moves[(i, j)] = piece.CAN_MOVE
            elif board[i][j].is_black != self.is_black:
                possibles_moves[(i, j)] = piece.CAN_KILL
        return possibles_moves
    
    
# test_board = [[None for _ in range(8)]for _ in range(8)]
# x = 4
# y = 4
# t = bishop(True, 1)
# t.show_movement(test_board, x, y)
