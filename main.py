class Field:
    def __init__(self, size, ships):
        self.size = size
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)
        self.ships_alive = ships

# тут корабли изначально скрыты, нужно передать True
    def display(self, show_ships=False):
        letters = "ABCDEFGHIJ"
        letter_string = "    "
        for letter in letters:
            letter_string += letter + " "

        print(letter_string)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

test = Field(10, 1)
test.display();