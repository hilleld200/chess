import src.Chess_pieces.Board as Board
import unittest

test_board = Board.init_board()

class test_init_board(unittest.TestCase):
    
    
    def test_board_y(self):
        self.assertEqual(len(test_board), 8)
    
    def test_board_x(self):
        self.assertEqual(len(test_board[0]), 8)
                
    def test_all_pieces_color(self):
        black = 0
        white = 0
        for i in test_board:
            for j in i:
                if j != None:
                    if j.is_black:
                        black += 1
                    else:
                        white += 1
        self.assertEqual(black, 16)
        self.assertEqual(white, 16)
        
    def test_pieces_type(self):
        correct_dict = {
            'pawn': 16,
            'knight': 4,
            'bishop': 4,
            'rook': 4,
            'queen': 2,
            'king': 2
        }
        type_dict = {}
        for i in test_board:
            piece_type = type(i).__name__
            if piece_type in type_dict:
                type_dict[piece_type] += 1
            else:
                type_dict[piece_type] = 1
            
