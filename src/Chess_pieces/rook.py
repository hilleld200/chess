import src.Chess_pieces.piece as piece

class rook(piece.chest_piece):
    
    def show_movement(self, board: list, x: int, y: int) -> dict:
        i: int = 1
        possibles_moves: dict = {}
        checks = []
        # check for the right side
        while x + i < piece.MAX_BOARD_SIZE:
            checks.append((x + i, y))
            if board[x + i][y] != None:
                break
            i += 1
        
        i = 1
        # check for the left side
        while x - i >= piece.MIN_BOARD_SIZE:
            checks.append((x - i, y))
            if board[x - i][y] != None:
                break
            i += 1

        i = 1
        # check for the down side
        while y + i < piece.MAX_BOARD_SIZE:
            checks.append((x, y + i))
            if board[x][y + i] != None:
                break
            i += 1
            
        i = 1    
        # check for the up side
        while y - i >= piece.MIN_BOARD_SIZE:
            checks.append((x, y - i))
            if board[x][y - i] != None:
                break
            i += 1
        
        for i, j in checks:
            if board[i][j] == None:
                possibles_moves[(i, j)] = piece.CAN_MOVE
            elif board[i][j].is_black != self.is_black:
                possibles_moves[(i, j)] = piece.CAN_KILL
        return possibles_moves