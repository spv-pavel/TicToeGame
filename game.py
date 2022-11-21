def print_data(d):
    print(' ', end=' ')
    for i in range(len(d[0])):
        print(i, end=' ')
    print('\n', end='')
    for ny, y in enumerate(range(len(d))):
        print(ny, end=' ')
        for x in range(len(d[y])):
            print(d[y][x], end=' ')
        print('\n', end='')


data = [['-' for x in range(0, 3)] for y in range(0, 3)]

print_data(data)
