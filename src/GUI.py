import tkinter as tk
import customtkinter as ctk
import pathlib


SQUARE_SIZE = 100



class ChessGUI:
    def __init__(self, click_callback: callable):
        self.window = ctk.CTk()
        self.window.title("Chess")
        self.window.geometry(f"{SQUARE_SIZE * 10}x{SQUARE_SIZE * 10}")
        self.canvas = ctk.CTkCanvas(self.window, width=SQUARE_SIZE * 8, height=SQUARE_SIZE * 8)
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
        self.window.bind("<Button-1>", click_callback)

    def draw_board(self):
        # Draw the squares
        for i in range(8):
            for j in range(8):
                color = "gray" if (i+j) % 2 == 0 else "white"
                self.canvas.create_rectangle(i*SQUARE_SIZE, j*SQUARE_SIZE, (i+1)*SQUARE_SIZE, (j+1)*SQUARE_SIZE, fill=color)

        # Draw the pieces
        self.pieces = {}
        self.pieces["A1"] = self.draw_piece("black-rook", 0, 0)
        self.pieces["B1"] = self.draw_piece("black-knight", 1, 0)
        self.pieces["C1"] = self.draw_piece("black-bishop", 2, 0)
        self.pieces["D"] = self.draw_piece("black-queen", 3, 0)
        self.pieces["E"] = self.draw_piece("black-king", 4, 0)
        self.pieces["C2"] = self.draw_piece("black-bishop", 5, 0)
        self.pieces["B2"] = self.draw_piece("black-knight", 6, 0)
        self.pieces["A2"] = self.draw_piece("black-rook", 7, 0)
        
        self.pieces["a1"] = self.draw_piece("white-rook", 0, 7)
        self.pieces["b1"] = self.draw_piece("white-knight", 1, 7)
        self.pieces["c1"] = self.draw_piece("white-bishop", 2, 7)
        self.pieces["d"] = self.draw_piece("white-queen", 3, 7)
        self.pieces["e"] = self.draw_piece("white-king", 4, 7)
        self.pieces["c2"] = self.draw_piece("white-bishop", 5, 7)
        self.pieces["b2"] = self.draw_piece("white-knight", 6, 7)
        self.pieces["a2"] = self.draw_piece("white-rook", 7, 7)
        
        for i in range(8):
            self.pieces["P " + str(i+1)] = self.draw_piece("black-pawn", i, 1)
            self.pieces["p " + str(i+1)] = self.draw_piece("white-pawn", i, 6)
            

    def draw_piece(self, piece_type, x, y):
        color = "gray" if (x+y) % 2 == 0 else "white"
        image = self.piece_images[piece_type]
        label = tk.Label(self.canvas, image=image, width=self.PIECE_SIZE, height=self.PIECE_SIZE,bg=color)
        label.image = image
        label.place(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE)
        return label

    def start_game(self, board):
        self.board = board
        self.draw_board()


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChessGUI()
    gui.start_game([])
    gui.run()