import src.Chess_pieces.piece as piece

class pawn(piece.chest_piece):
    
    def show_movement(self, board: list, x: int, y: int) -> dict:
        possibles_moves: dict = {}
        add_y = 1 if self.is_black else -1
        #TODO: add first move
        #TODO: add end of board
        if board[y + add_y][x] == None:
            possibles_moves[(y + add_y, x)] = piece.CAN_MOVE
        try:
            if board[y + (add_y*2)][x-1].is_black != self.is_black:
                possibles_moves[(y + (add_y*2), x-1)] = piece.CAN_KILL
        except (AttributeError, IndexError):
            pass
        try:
            if board[y + (add_y*2)][x+1].is_black != self.is_black:
                possibles_moves[(y + (add_y*2), x+1)] = piece.CAN_KILL
        except (AttributeError, IndexError):
            pass
        
        
        
        return possibles_moves