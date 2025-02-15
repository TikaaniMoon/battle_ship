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


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    def is_valid_ship_placement(self, field, coords, ship_length=1):
        x, y = coords
        for j in range(-1, 2):
            for k in range(-1, 2):
                new_x, new_y = x + j, y + k
                if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                    return False
        return True

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display(show_ships=True)

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
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
