from src.Chess_pieces import knight, board
def print_board_movement(board: list, movements: dict) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if (i, j) in movements:
                # print(movements[(i, j)], end=" ")
                print(f"({i},{j})", end=" ")
            # else:
            #     print(0, end=" ")
        print()

def main():
    test_board = [[None for _ in range(8)]for _ in range(8)]
    x = 4
    y = 4
    quee = knight.knight(True, 1)

    # print_board_movement(test_board, quee.show_movement(test_board, x, y))



if __name__ == "__main__":
    main()
