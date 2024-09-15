import src.Chess_pieces.piece as piece

class pawn(piece.chest_piece):
    
    def show_movement(self, board: list, x: int, y: int) -> dict:
        possibles_moves: dict = {}
        add_y = 1 if self.is_black else -1
        #TODO: add first move
        #TODO: add end of board
        if board[x + add_y][y] == None:
            possibles_moves[(x + add_y, y)] = piece.CAN_MOVE
        try:
            if board[x + 1 + add_y][y].is_black != self.is_black:
                possibles_moves[(x + 1 + add_y, y)] = piece.CAN_KILL
        except AttributeError:
            pass
        try:
            if board[x - 1 + add_y][y].is_black != self.is_black:
                possibles_moves[(x - 1 + add_y, y)] = piece.CAN_KILL
        except AttributeError:
            pass
        
        
        
        return possibles_moves