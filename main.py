import random
import sys

sys.stdout.reconfigure(encoding='utf-8')


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]
        self.ships_alive = ships

    def display(self, show_ships=False):
        letters = "ABCDEFGHIJ"
        print("    " + " ".join(letters))
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell == 'X':
                    display_row += "X "
                elif cell == '*':
                    display_row += "* "
                elif cell == 'S' and show_ships:
                    display_row += "■ "
                else:
                    display_row += "O "
            print(f"{i + 1:2}  {display_row}")

    def place_ship_manual(self, ship_length):
        while True:
            try:
                coords = input(f'Введите начальные координаты (например, A1) для корабля длины {ship_length}: ').upper()
                direction = input('Введите направление (H - горизонтально, V - вертикально): ').upper()
                x = "ABCDEFGHIJ".index(coords[0])
                y = int(coords[1:]) - 1

                if self.is_valid_ship_placement((y, x), ship_length, direction):
                    for i in range(ship_length):
                        if direction == 'H':
                            self.grid[y][x + i] = "S"
                        else:
                            self.grid[y + i][x] = "S"
                    return
                else:
                    print("Неверная позиция! Попробуйте снова.")
            except (ValueError, IndexError):
                print("Некорректный ввод. Попробуйте снова.")

    def is_valid_ship_placement(self, coords, ship_length, direction):
        y, x = coords
        for i in range(ship_length):
            # проверка что в этой точке корабль можно расположить
            new_x = x + i if direction == 'H' else x
            new_y = y if direction == 'H' else y + i
            if new_x >= self.size or new_y >= self.size or self.grid[new_y][new_x] == "S":
                return False

            # тут я проверяю что вокруг корабля нет других кораблей по вертикали и потом по горизонтали
            for offset_y in range(-1, 2):
                for offset_x in range(-1, 2):
                    neighbor_x = new_x + offset_x
                    neighbor_y = new_y + offset_y

                    if 0 <= neighbor_x < self.size and 0 <= neighbor_y < self.size:

                        if self.grid[neighbor_y][neighbor_x] == "S":
                            return False
        return True


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.player_field = Field(self.size, len(self.ships))
        self.computer_field = Field(self.size, len(self.ships))

    def place_ships_randomly(self, field, ships):
        for ship_length in ships:
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                direction = random.choice(['H', 'V'])
                if field.is_valid_ship_placement(coords, ship_length, direction):
                    for i in range(ship_length):
                        if direction == 'H':
                            field.grid[coords[0]][coords[1] + i] = "S"
                        else:
                            field.grid[coords[0] + i][coords[1]] = "S"
                    placed = True

    def setup_player_field(self):
        choice = input("Хотите расставить корабли вручную? (Y/N): ").upper()
        if choice == 'Y':
            for ship_length in self.ships:
                self.player_field.display(show_ships=True)
                self.player_field.place_ship_manual(ship_length)
        else:
            self.place_ships_randomly(self.player_field, self.ships)

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display(show_ships=True)

        print("Ваша расстановка кораблей:")
        self.setup_player_field()
        self.player_field.display(show_ships=True)

        while True:
            x = input('Введите координату x - букву: ').upper()
            y = int(input('Введите координату y - цифру: '))
            self.player_turn(x, y)
            self.show_fields()

            if self.computer_field.ships_alive == 0:
                print('Вы победили! Все корабли компьютера потоплены')
                break

            self.computer_turn()
            self.show_fields()

            if self.player_field.ships_alive == 0:
                print('Вы проиграли! Все ваши корабли потоплены')
                break

    def player_turn(self, x, y):
        x = "ABCDEFGHIJ".index(x)
        y -= 1

        if self.computer_field.grid[y][x] == 'S':
            print('Вы попали!')
            self.computer_field.grid[y][x] = 'X'
            self.computer_field.ships_alive -= 1
        elif self.computer_field.grid[y][x] is None:
            print('Промах!')
            self.computer_field.grid[y][x] = '*'
        else:
            print('Вы уже стреляли в эту точку!')

    def computer_turn(self):
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.player_field.grid[y][x] not in ['X', '*']:
                break

        if self.player_field.grid[y][x] == 'S':
            print('Компьютер попал!')
            self.player_field.grid[y][x] = 'X'
            self.player_field.ships_alive -= 1
        else:
            print('Компьютер промахнулся!')
            self.player_field.grid[y][x] = '*'

    def show_fields(self):
        print("\nПоле компьютера:")
        self.computer_field.display(show_ships=True)
        print("\nВаше поле:")
        self.player_field.display(show_ships=True)


if __name__ == "__main__":
    game = BattleshipGame()
    game.play()