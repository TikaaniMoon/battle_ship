import random

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


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):

        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display()

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(show_ships=True)

    def player_turn(self, x, y):
        x = "ABCDEFGHIJ".index(x)
        y -= 1

        if self.computer_field.grid[y][x] == 'S':
            print('Вы попали!')
            self.computer_field.grid[y][x] = 'x'
            self.computer_field.ships_alive -= 1
        else:
            print('Промах!')



