def print_data(data_):
    print(' ', end=' ')
    for i_ in range(len(data_[0])):
        print(i_, end=' ')
    print('\n', end='')
    for ny, y in enumerate(range(len(data_))):
        print(ny, end=' ')
        for x in range(len(data_[y])):
            print(data_[y][x], end=' ')
        print('\n', end='')


def go(player_):
    yx = list(map(int, (str.split(input(f'Ход игрока {player_}:')))))
    return yx


def player_change(player_):
    if player_ == 'x':
        player_ = 'o'
    else:
        player_ = 'x'
    return player_


def victory(data_):
    for y in data_:
        if y == ['x', 'x', 'x']:
            y = 1
    pass


data = [['-' for x in range(0, 3)] for y in range(0, 3)]
print_data(data)
print('Введите координаты y x через пробел!')
player = 'x'

for i in range(9):
    y, x = go(player)
    data[y][x] = player
    print_data(data)
    player = player_change(player)
