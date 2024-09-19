from src.GUI import ChessGUI, SQUARE_SIZE, Piece_Label


class UserInputError(Exception):
    pass

class GameError(Exception):
    pass

class GAME:
    
    def start_game(self, board):
        gui = ChessGUI(self.board_click, self.piece_click)
        self.gui = gui
        self.canvas = gui.canvas
        self.board = board
        self.is_black_turn = False
        self.movement = {}
        
        
        gui.start_game()
        gui.run()
    
    def board_click(self, event):
        x = event.x 
        y = event.y 
        print("board event")
        print(x, y)
        
    def piece_click(self, event):
        piece_label = event.widget
        x = piece_label.winfo_x() // SQUARE_SIZE
        y = piece_label.winfo_y() // SQUARE_SIZE
        
        piece = self.board[y][x]
        if piece is None:
            raise GameError("Something went wrong\nin function piece_click")
        
        # check if can eat
        if (y,x) in self.movement:
            self.piece_eat(x,y)
            return
        
        if(self.is_black_turn != piece.is_black):
            # it not the user piece
            return
        
        self.piece_movement(x, y)
        print("piece event")
        print(x, y)
        
    def piece_movement(self, x, y):
        piece_to_move = self.board[y][x]
        self.selected_piece = (x, y)
        for m_y,m_x in self.movement:
            self.color_square(m_x, m_y)
        self.movement = piece_to_move.show_movement(self.board, x,y)
        for y,x in self.movement:
            color = "yellow" if self.movement[(y,x)] == 1 else "red"
            self.color_square(x, y, color)
        
    def color_square(self, x:int, y:int, color:str = None)-> None:
        if color == None:
            color = "gray" if (x+y) % 2 == 0 else "white"
        item = self.get_piece(x, y)
        if item != None:
            item.config(bg = color)
            return
        self.canvas.create_rectangle(x * SQUARE_SIZE, y * SQUARE_SIZE, (x + 1) * SQUARE_SIZE, (y + 1) * SQUARE_SIZE, fill = color)
    
    def get_piece(self, x:int, y:int) -> object:
        for widget in self.canvas.winfo_children():
            if isinstance(widget, Piece_Label):
                if widget.winfo_x() // SQUARE_SIZE == x and widget.winfo_y() // SQUARE_SIZE == y:
                    return widget
        return None
        
    def piece_eat(self, x:int, y:int) -> None:
        eaten_piece = self.get_piece(x, y)
        piece_to_move = self.get_piece(self.selected_piece[0], self.selected_piece[1])
        if eaten_piece == None:
            GameError("Something went wrong\nin function piece_eat")
        self.canvas.delete(eaten_piece)
        self.move_piece(piece_to_move, x, y)
        self.reset_movement()
        
    def reset_movement(self) -> None:
        for y,x in self.movement:
            self.color_square(x, y)
        self.movement = {}
        
    def move_piece(self, piece_to_move, x, y):
        piece_to_move.place(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE)
        self.color_square(x, y)
        self.is_black_turn = not self.is_black_turn
        
        
    

    