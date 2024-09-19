import tkinter as tk
import customtkinter as ctk
import pathlib


SQUARE_SIZE = 100



class ChessGUI:
    def __init__(self, canvas_click: callable, piece_click: callable):
        self.window = ctk.CTk()
        self.window.title("Chess")
        self.window.geometry(f"{SQUARE_SIZE * 8}x{SQUARE_SIZE * 8}")
        self.canvas = Canvas_Board(canvas_click,self.window, width=SQUARE_SIZE * 8, height=SQUARE_SIZE * 8)
        self.canvas.pack()
        self.window.update_idletasks()
        self.PIECE_SIZE = SQUARE_SIZE 
        
        path = str(pathlib.Path(__file__).parent.resolve()) + "/chess-pieces/"
        
        self.piece_images = {}
        self.piece_images["black-pawn"] = tk.PhotoImage(file=path + "black-pawn.png")
        self.piece_images["black-rook"] = tk.PhotoImage(file=path + "black-rook.png")
        self.piece_images["black-knight"] = tk.PhotoImage(file=path + "black-knight.png")
        self.piece_images["black-bishop"] = tk.PhotoImage(file=path + "black-bishop.png")
        self.piece_images["black-queen"] = tk.PhotoImage(file=path + "black-queen.png")
        self.piece_images["black-king"] = tk.PhotoImage(file=path + "black-king.png")
        self.piece_images["white-pawn"] = tk.PhotoImage(file=path + "white-pawn.png")
        self.piece_images["white-rook"] = tk.PhotoImage(file=path + "white-rook.png")
        self.piece_images["white-knight"] = tk.PhotoImage(file=path + "white-knight.png")
        self.piece_images["white-bishop"] = tk.PhotoImage(file=path + "white-bishop.png")
        self.piece_images["white-queen"] = tk.PhotoImage(file=path + "white-queen.png")
        self.piece_images["white-king"] = tk.PhotoImage(file=path + "white-king.png")

        # Bind the left mouse button click event to a function
        self.piece_click = piece_click

    def draw_board(self):
        # Draw the squares
        for i in range(8):
            for j in range(8):
                color = "gray" if (i+j) % 2 == 0 else "white"
                self.canvas.create_rectangle(i*SQUARE_SIZE, j*SQUARE_SIZE, (i+1)*SQUARE_SIZE, (j+1)*SQUARE_SIZE, fill=color)

        # Draw the pieces
        self.pieces = {}
        self.pieces["A1"] = self.draw_piece("black-rook", 0, 0, "A1")
        self.pieces["B1"] = self.draw_piece("black-knight", 1, 0, "B1")
        self.pieces["C1"] = self.draw_piece("black-bishop", 2, 0, "C1")
        self.pieces["D"] = self.draw_piece("black-queen", 3, 0, "D")
        self.pieces["E"] = self.draw_piece("black-king", 4, 0, "E")
        self.pieces["C2"] = self.draw_piece("black-bishop", 5, 0, "C2")
        self.pieces["B2"] = self.draw_piece("black-knight", 6, 0, "B2")
        self.pieces["A2"] = self.draw_piece("black-rook", 7, 0, "A2")
        
        self.pieces["a1"] = self.draw_piece("white-rook", 0, 7, "a1")
        self.pieces["b1"] = self.draw_piece("white-knight", 1, 7, "b1")
        self.pieces["c1"] = self.draw_piece("white-bishop", 2, 7, "c1")
        self.pieces["d"] = self.draw_piece("white-queen", 3, 7, "d")
        self.pieces["e"] = self.draw_piece("white-king", 4, 7, "e")
        self.pieces["c2"] = self.draw_piece("white-bishop", 5, 7, "c2")
        self.pieces["b2"] = self.draw_piece("white-knight", 6, 7, "b2")
        self.pieces["a2"] = self.draw_piece("white-rook", 7, 7, "a2")
        
        for i in range(8):
            self.pieces["P " + str(i+1)] = self.draw_piece("black-pawn", i, 1, "P " + str(i+1))
            self.pieces["p " + str(i+1)] = self.draw_piece("white-pawn", i, 6, "p " + str(i+1))
    
    # def check_if_have_piece(self, x, y):
    #     for piece in self.pieces:
    #         if self.pieces[piece].winfo_x() // self.PIECE_SIZE == x and self.pieces[piece].winfo_y() // self.PIECE_SIZE == y:
    #             return piece
    #         else:
    #             return None

    def draw_piece(self, piece_type:str, x:int, y:int, id:str) -> object:
        image = self.piece_images[piece_type]
        label = Piece_Label(self.canvas, x, y, image, self.PIECE_SIZE, self.piece_click, id)
        label.place(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE)
        return label

    def start_game(self):
        self.draw_board()


    def run(self):
        self.window.mainloop()


class Piece_Label(tk.Label):
    def __init__(self, master, x:int, y:int, image:tk.PhotoImage, piece_size:int, click_callback: callable, id:str):
        color = "gray" if (x+y) % 2 == 0 else "white"
        super().__init__(master, image=image, width=piece_size, height=piece_size, bg=color)
        self.place(x=x * SQUARE_SIZE, y=y * SQUARE_SIZE)
        self.image = image
        self.id = id
        
        self.bind("<Button-1>", click_callback)
        
   
class Canvas_Board(tk.Canvas):
    def __init__(self, click_event, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.bind("<Button-1>", click_event)



