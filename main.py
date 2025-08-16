board_size = 6
# houses = [0] * (board_size + 1) * 2

def index(x, y):
    if x < 0:
        return x + (y + 1) * (board_size + 1)
    else:
        return x + y * (board_size + 1)

def is_mom(pos):
    return (pos + 1) % (board_size + 1) == 0

def spot(pos):
    return (pos) % ((board_size + 1) * 2)

def opposite(x):
    return (board_size * 2) - x

def swap_player(player):
    return 'A' if player == 'B' else 'B'

def print_board(houses):
    print('+----', end='')
    for _ in range(board_size):
        print('+----', end='')
    print('+----+')

    print('|    ', end='')
    for _ in range(board_size):
        print('|    ', end='')
    print('|    |')

    print('|    ', end='')
    for i in reversed(range(board_size)):
        print(f'| {houses[index(i, 0)]:>2} ', end='')
    print('|    |')

    print('|    ', end='')
    for _ in range(board_size):
        print('|    ', end='')
    print('|    |')

    print(f'| {houses[index(-1, 0)]:>2} ', end='')
    for _ in range(board_size):
        print('+----', end='')
    print(f'+ {houses[index(-1, 1)]:>2} |')

    print('|    ', end='')
    for _ in range(board_size):
        print('|    ', end='')
    print('|    |')

    print('|    ', end='')
    for i in range(board_size):
        print(f'| {houses[index(i, 1)]:>2} ', end='')
    print('|    |')

    print('|    ', end='')
    for _ in range(board_size):
        print('|    ', end='')
    print('|    |')

    print('+----', end='')
    for _ in range(board_size):
        print('+----', end='')
    print('+----+')

    print('     ', end='')
    for i in range(board_size):
        print(f'| {i + 1:>2} ', end='')
    print('|     ')

    print('     ', end='')
    for _ in range(board_size):
        print('+----', end='')
    print('+     ')

def move(houses, pos):
    if houses[pos] < 0:
        return

    i = 0
    pieces = houses[pos]
    houses[pos] = 0
    while pieces > 0:
        i += 1
        if is_mom(pos + i) and not ((pos < 7) == (spot(pos + i) < 7)):
            continue
        else:
            houses[spot(pos + i)] += 1
        pieces -= 1

        if pieces == 0 and is_mom(pos + i):
            print("One more move!")

def main():
    player = 'A'
    # houses = [
    #     4, 4, 4, 4, 4, 4,
    #     0,
    #     4, 4, 4, 4, 4, 14,
    #     0,
    # ]

    houses = ([4] * board_size + [0]) * 2
    print_board(houses)

    num = int(input("Position: "))

    move(houses, num + (board_size if player == 'A' else 0))
    print_board(houses)

if __name__ == '__main__':
    main()
