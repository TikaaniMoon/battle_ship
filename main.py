class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)

    def display(self, show_ships=False):

        # вывод строки с буквами
        letters = 'ABCDEFGHIJ'
        letter_space = '     '

        for letter in letters:
            letter_space += letter + ' '

        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    display_row += 'O '
                else:
                    display_row += '■ '
            if i + 1 != 10:
                print(i + 1, '', display_row)
            else:
                print(i + 1, '', display_row)

Titanik = Field(10, 1)
Titanik.display()
