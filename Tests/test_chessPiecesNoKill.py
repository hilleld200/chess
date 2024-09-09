from src.Chess_pieces import bishop, king, knight, pawn, queen, rook
import unittest

class test_chessPiecesNoKill(unittest.TestCase):
    
    test_board = [[None for _ in range(8)]for _ in range(8)]
    x = 4
    y = 4
    
    def test_rook(self):
        correct_dict = {
            (0, 4): 1,
            (1, 4): 1,
            (2, 4): 1,
            (3, 4): 1,
            (5, 4): 1,
            (6, 4): 1,
            (7, 4): 1,
            (4, 0): 1,
            (4, 1): 1,
            (4, 2): 1,
            (4, 3): 1,
            (4, 5): 1,
            (4, 6): 1,
            (4, 7): 1,
        }
        t = rook.rook(True, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)

    def test_bishop(self):
        correct_dict = {
            (0,0): 1,
            (1,1): 1,
            (2,2): 1,
            (3,3): 1,
            (5,5): 1,
            (6,6): 1,
            (7,7): 1,
            (1,7): 1,
            (2,6): 1,
            (3,5): 1,
            (5,3): 1,
            (6,2): 1,
            (7,1): 1
        }
        t = bishop.bishop(True, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)

    def test_queen(self):
        correct_dict = {
            (0, 0): 1,
            (0, 4): 1,
            (1, 1): 1,
            (1, 4): 1,
            (1, 7): 1,
            (2, 2): 1,
            (2, 4): 1,
            (2, 6): 1,
            (3, 3): 1,
            (3, 4): 1,
            (3, 5): 1,
            (4, 0): 1,
            (4, 1): 1,
            (4, 2): 1,
            (4, 3): 1,
            (4, 5): 1,
            (4, 6): 1,
            (4, 7): 1,
            (5, 3): 1,
            (5, 4): 1,
            (5, 5): 1,
            (6, 2): 1,
            (6, 4): 1,
            (6, 6): 1,
            (7, 1): 1,
            (7, 4): 1,
            (7, 7): 1
        }
        t = queen.queen(True, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)

    def test_king(self):
        correct_dict = {
            (3,5): 1,
            (4,5): 1,
            (5,5): 1,
            (3,3): 1,
            (4,3): 1,
            (5,3): 1,
            (3,4): 1,
            (5,4): 1
        }
        t = king.king(True, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)

    def test_knight(self):
        correct_dict = {
            (2,3): 1,
            (3,2): 1,
            (2,5): 1,
            (3,6): 1,
            (5,2): 1,
            (6,3): 1,
            (5,6): 1,
            (6,5): 1
        }
        t = knight.knight(True, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)
        
    def test_pawn(self):
        correct_dict = {
            (4,3): 1,
        }
        t = pawn.pawn(False, 1)
        self.assertDictEqual(t.show_movement(self.test_board, self.x, self.y), correct_dict)