from random import sample
SIZE = 9
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.neighbor_mines = 0
        self.is_open = False
        self.is_flagged = False
        self.symbol = "?"
        self.inside_symbol = "?"

class Board:
    def __init__(self, first_x, first_y):
        self.first_x = first_x
        self.first_y = first_y
        self.mines = []
        self.cells = [[Cell(i, j) for i in range(9)] for j in range(9)]

    def put_mines(self):
        all_c = [(i, j) for i in range(9) for j in range(9) if (i, j) != (self.first_x - 1, self.first_y - 1)]
        mine = sample(all_c, 10)
        for i, j in mine:
            self.cells[i][j].is_mine = True
            self.mines.append(self.cells[i][j])
            self.cells[i][j].inside_symbol = "*"

    def count_neighbors(self):
        for i in range(9):
            for j in range(9):
                count_mines = 0
                if self.cells[i][j].is_mine:
                    continue
                if i + 1 < 9:
                    if j + 1 < 9:
                        if self.cells[i + 1][j + 1].is_mine or self.cells[i][j + 1].is_mine or self.cells[i + 1][j].is_mine:
                            count_mines += 1
                    if j - 1 >= 0:
                        if self.cells[i + 1][j - 1].is_mine or self.cells[i][j - 1].is_mine:
                            count_mines += 1
                if i - 1 >= 0:
                    if j + 1 < 9:
                        if self.cells[i - 1][j].is_mine or self.cells[i - 1][j + 1].is_mine:
                            count_mines += 1
                    if j - 1 >= 0:
                        if self.cells[i - 1][j - 1].is_mine:
                            count_mines += 1

                self.cells[i][j].neighbor_mines = count_mines
                self.cells[i][j].inside_symbol = f"{count_mines}"

    def print_board(self):
        print("  1 2 3 4 5 6 7 8 9 ")
        for i in range(9):
            print(f"{i + 1}", end = " ")
            for j in range(9):
                if i + 1 == self.first_x and j + 1 == self.first_y:
                    if self.cells[i][j].inside_symbol != "0":
                       print(f"{self.cells[i][j].inside_symbol}", end = " ")
                    else:
                else:
                    print(self.cells[i][j].symbol, end = " ")
            print()

    def open_cell(self, x, y):
        for i in range(SIZE):
            for j in range(SIZE):
                if i == x - 1 and j == y - 1:
                    if self.cells[i][j].is_mine:
                        print("Мина!\nИгра окончена")
                    elif self.cells[i][j].inside_symbol


b = Board(6, 8)
b.put_mines()
b.count_neighbors()
b.print_board()