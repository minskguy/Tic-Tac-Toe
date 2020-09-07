def coordinate_converter(point):
    if point[0] == "1" and point[1] == "1":
        return 6
    elif point[0] == "1" and point[1] == "2":
        return 3
    elif point[0] == "1" and point[1] == "3":
        return 0
    elif point[0] == "2" and point[1] == "1":
        return 7
    elif point[0] == "2" and point[1] == "2":
        return 4
    elif point[0] == "2" and point[1] == "3":
        return 1
    elif point[0] == "3" and point[1] == "1":
        return 8
    elif point[0] == "3" and point[1] == "2":
        return 5
    elif point[0] == "3" and point[1] == "3":
        return 2


def draw_check(state):
    if state.count('_') == 0:
        return True
    else:
        return False


def impossible_check(state):
    if abs(state.count('X') - state.count('O')) >= 2:
        return True
    if x_wins_check(state) and o_wins_check(state):
        return True


def not_finished_check(state):
    if state.count('_') != 0:
        return True
    else:
        return False


def x_wins_check(state):
    if (state[0] == state[1] == state[2] == 'X' or state[3] == state[4] == state[5] == 'X'
            or state[6] == state[7] == state[8] == 'X'
            or state[0] == state[3] == state[6] == 'X'
            or state[1] == state[4] == state[7] == 'X'
            or state[2] == state[5] == state[8] == 'X'
            or state[0] == state[4] == state[8] == 'X'
            or state[2] == state[4] == state[6] == 'X'):
        return True
    else:
        return False


def o_wins_check(state):
    if (state[0] == state[1] == state[2] == 'O'
            or state[3] == state[4] == state[5] == 'O'
            or state[6] == state[7] == state[8] == 'O'
            or state[0] == state[3] == state[6] == 'O'
            or state[1] == state[4] == state[7] == 'O'
            or state[2] == state[5] == state[8] == 'O'
            or state[0] == state[4] == state[8] == 'O'
            or state[2] == state[4] == state[6] == 'O'):
        return True
    else:
        return False


def game_state(state):
    if impossible_check(state):
        print("Impossible")
    elif x_wins_check(state):
        print("X wins")
    elif o_wins_check(state):
        print("O wins")
    elif draw_check(state):
        print("Draw")
    else:
        print("Game not finished")


def print_field(cells):
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def set_coordinates(cells, point, x_turn):
    numbers = ["1", "2", "3"]
    while True:
        if len(point) != 2:
            print("You should enter numbers!")
            print("Enter the coordinates:")
            point = input().split()
        elif point[0].isalpha() or point[1].isalpha():
            print("You should enter numbers!")
            print("Enter the coordinates:")
            point = input().split()
        elif point[0] not in numbers or point[1] not in numbers:
            print("Coordinates should be from 1 to 3!")
            print("Enter the coordinates:")
            point = input().split()
        elif cells[coordinate_converter(point)] == "X" or cells[coordinate_converter(point)] == "O":
            print("This cell is occupied! Choose another one!")
            print("Enter the coordinates:")
            point = input().split()
        else:
            if x_turn:
                cells[coordinate_converter(point)] = "X"
            else:
                cells[coordinate_converter(point)] = "O"
            return


field = ["_" for _ in range(9)]
print_field(field)
player = True

while all([not draw_check(field), not x_wins_check(field), not o_wins_check(field)]):
    print("Enter the coordinates:")
    coordinates = input().split()
    set_coordinates(field, coordinates, player)
    player = False if player else True
    print_field(field)

game_state(field)
