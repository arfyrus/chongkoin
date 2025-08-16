import random as rd
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

def my_house(pos, i):
    return ((pos < 7) == (spot(pos + i) < 7))

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
    if houses[pos] <= 0:
        print("Move again!")
        return True

    i = 0
    pieces = houses[pos]
    houses[pos] = 0
    while pieces > 0:
        i += 1
        if is_mom(pos + i) and not my_house(pos, i):
            continue
        else:
            houses[spot(pos + i)] += 1
        pieces -= 1

        if pieces == 0 and is_mom(pos + i) and check_empty(houses) == 'N':
            print("One more move!")
            return True

        if pieces == 0 and houses[spot(pos + i)] == 1 and my_house(pos, i) and house[opposite(spot(pos + i))] > 0:
            print("Capture!")
            piece_num = 1 + houses[opposite(spot(pos + i))]
            houses[opposite(spot(pos + i))] = 0
            houses[spot(pos + i)] = 0
            houses[index(-1, (0 if pos < 7 else 1))] += piece_num

    return False

def check_empty(houses):
    a_win = True
    for i in range(board_size):
        if houses[i + board_size + 1] > 0:
            a_win = False
            break

    if a_win:
        return 'A'

    b_win = True
    for i in range(board_size):
        if houses[i] > 0:
            b_win = False
            break

    if b_win:
        return 'B'

    return 'N'

def main():
    player = 'A'
    # houses = [
    #     4, 4, 4, 4, 4, 4,
    #     0,
    #     0, 0, 1, 0, 0, 0,
    #     9,
    # ]

    houses = ([4] * board_size + [0]) * 2

    while check_empty(houses) == 'N':
        print_board(houses)

        num = int(input("Position: ")) if player == 'A' else rd.randint(0, board_size - 1)

        again = move(houses, num + (board_size if player == 'A' else 0))
        if not again:
            player = swap_player(player)

    print(f"{check_empty(houses)} wins!")
    print_board(houses)

if __name__ == '__main__':
    main()
