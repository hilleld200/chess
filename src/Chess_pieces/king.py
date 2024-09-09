import src.Chess_pieces.piece as piece

class king(piece.chest_piece):
    
    def show_movement(self, board: list, x: int, y: int) -> dict:
        possibles_moves: dict = {}
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < piece.MIN_BOARD_SIZE or x + i >= piece.MAX_BOARD_SIZE or y + j < piece.MIN_BOARD_SIZE or y + j >= piece.MAX_BOARD_SIZE:
                    continue
                if board[x + i][y + j] == None:
                    possibles_moves[(x + i, y + j)] = piece.CAN_MOVE
                elif board[x + i][y + j].is_black != self.is_black:
                    possibles_moves[(x + i, y + j)] = piece.CAN_KILL
        return possibles_moves