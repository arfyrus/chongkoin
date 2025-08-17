import random as rd
import curses

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

# def old_print_board(houses):
#     print('+----', end='')
#     for _ in range(board_size):
#         print('+----', end='')
#     print('+----+')
#
#     print('|    ', end='')
#     for _ in range(board_size):
#         print('|    ', end='')
#     print('|    |')
#
#     print('|    ', end='')
#     for i in reversed(range(board_size)):
#         print(f'| {houses[index(i, 0)]:>2} ', end='')
#     print('|    |')
#
#     print('|    ', end='')
#     for _ in range(board_size):
#         print('|    ', end='')
#     print('|    |')
#
#     print(f'| {houses[index(-1, 0)]:>2} ', end='')
#     for _ in range(board_size):
#         print('+----', end='')
#     print(f'+ {houses[index(-1, 1)]:>2} |')
#
#     print('|    ', end='')
#     for _ in range(board_size):
#         print('|    ', end='')
#     print('|    |')
#
#     print('|    ', end='')
#     for i in range(board_size):
#         print(f'| {houses[index(i, 1)]:>2} ', end='')
#     print('|    |')
#
#     print('|    ', end='')
#     for _ in range(board_size):
#         print('|    ', end='')
#     print('|    |')
#
#     print('+----', end='')
#     for _ in range(board_size):
#         print('+----', end='')
#     print('+----+')
#
#     print('     ', end='')
#     for i in range(board_size):
#         print(f'| {i + 1:>2} ', end='')
#     print('|     ')
#
#     print('     ', end='')
#     for _ in range(board_size):
#         print('+----', end='')
#     print('+     ')

# def line_print_board(stdscr, houses):
#     stdscr.addch(curses.ACS_ULCORNER)
#     for _ in range(4):
#         stdscr.addch(curses.ACS_HLINE)
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_TTEE)
#         for _ in range(4):
#             stdscr.addch(curses.ACS_HLINE)
#     stdscr.addch(curses.ACS_TTEE)
#     for _ in range(4):
#         stdscr.addch(curses.ACS_HLINE)
#     stdscr.addch(curses.ACS_URCORNER)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for i in reversed(range(board_size)):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr(f' {houses[index(i, 0)]:>2} ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr(f' {houses[index(-1, 0)]:>2} ')
#     for i in range(board_size):
#         if i == 0:
#             stdscr.addch(curses.ACS_SSSB)
#         else:
#             stdscr.addch(curses.ACS_SSSS)
#         for _ in range(4):
#             stdscr.addch(curses.ACS_HLINE)
#     stdscr.addch(curses.ACS_SBSS)
#     stdscr.addstr(f' {houses[index(-1, 1)]:>2} ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for i in range(board_size):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr(f' {houses[index(i, 1)]:>2} ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_VLINE)
#         stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addstr('    ')
#     stdscr.addch(curses.ACS_VLINE)
#     stdscr.addch('\n')
#
#     stdscr.addch(curses.ACS_SSBB)
#     for _ in range(4):
#         stdscr.addch(curses.ACS_HLINE)
#     for _ in range(board_size):
#         stdscr.addch(curses.ACS_SSBS)
#         for _ in range(4):
#             stdscr.addch(curses.ACS_HLINE)
#     stdscr.addch(curses.ACS_SSBS)
#     for _ in range(4):
#         stdscr.addch(curses.ACS_HLINE)
#     stdscr.addch(curses.ACS_SBBS)
#     stdscr.addch('\n')
#
#     # print('     ', end='')
#     # for i in range(board_size):
#     #     print(f'| {i + 1:>2} ', end='')
#     # print('|     ')
#     #
#     # print('     ', end='')
#     # for _ in range(board_size):
#     #     print('+----', end='')
#     # print('+     ')

def print_board(stdscr, houses, choice):
    # Horizontal lines
    stdscr.hline(0, 0, curses.ACS_BSBS, (board_size + 2) * 5)
    stdscr.hline(8, 0, curses.ACS_BSBS, (board_size + 2) * 5)
    stdscr.hline(4, 5, curses.ACS_BSBS, (board_size) * 5)

    # Vertical lines
    stdscr.addch(0, 0, curses.ACS_BSSB)
    stdscr.vline(1, 0, curses.ACS_SBSB, 7)
    stdscr.addch(8, 0, curses.ACS_SSBB)
    for i in range(board_size):
        stdscr.addch(0, (i + 1) * 5, curses.ACS_BSSS)
        stdscr.vline(1, (i + 1) * 5, curses.ACS_SBSB, 7)
        stdscr.addch(8, (i + 1) * 5, curses.ACS_SSBS)
    stdscr.addch(0, (board_size + 1) * 5, curses.ACS_BSSS)
    stdscr.vline(1, (board_size + 1) * 5, curses.ACS_SBSB, 7)
    stdscr.addch(8, (board_size + 1) * 5, curses.ACS_SSBS)
    stdscr.addch(0, (board_size + 2) * 5, curses.ACS_BBSS)
    stdscr.vline(1, (board_size + 2) * 5, curses.ACS_SBSB, 7)
    stdscr.addch(8, (board_size + 2) * 5, curses.ACS_SBBS)

    # Intersection points
    stdscr.addch(4, 5, curses.ACS_SSSB)
    for i in range(board_size - 1):
        stdscr.addch(4, (i + 2) * 5, curses.ACS_SSSS)
    stdscr.addch(4, (board_size + 1) * 5, curses.ACS_SBSS)

    # Values
    ## Mothers
    stdscr.addstr(4, 2, f'{houses[index(-1, 0)]:>2}')
    stdscr.addstr(4, (board_size + 1) * 5 + 2, f'{houses[index(-1, 1)]:>2}')

    ## Children
    for i in range(board_size):
        ### Top
        stdscr.addstr(2, (i + 1) * 5 + 2, f'{houses[index(board_size - i - 1, 0)]:>2}')

        ### Bottom
        colour = 2 if i == choice else 1

        #### Fill
        for n in range(3):
            stdscr.hline(5 + n, (i + 1) * 5 + 1, ' ', 4, curses.color_pair(colour))

        stdscr.addstr(6, (i + 1) * 5 + 2, f'{houses[index(i, 1)]:>2}', curses.color_pair(colour))


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
            # print("One more move!")
            return True

        if pieces == 0 and houses[spot(pos + i)] == 1 and my_house(pos, i) and houses[opposite(spot(pos + i))] > 0:
            # print("Capture!")
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

# def old_main(stdscr):
#     player = 'A'
#     # houses = [
#     #     4, 4, 4, 4, 4, 4,
#     #     0,
#     #     0, 0, 1, 0, 0, 0,
#     #     9,
#     # ]
#
#     houses = ([4] * board_size + [0]) * 2
#
#     while check_empty(houses) == 'N':
#         print_board(houses)
#
#         num = int(input("Position: ")) if player == 'A' else rd.randint(0, board_size - 1)
#
#         again = move(houses, num + (board_size if player == 'A' else 0))
#         if not again:
#             player = swap_player(player)
#
#     print_board(houses)
#
#     winner = check_empty(houses)
#     for i in range(board_size):
#         side = 0 if winner == 'A' else 1
#         houses[index(-1, side)] += houses[index(i, side)]
#         houses[index(i, side)] = 0
#
#     print_board(houses)
#
#     if houses[index(-1, 1)] > houses[index(-1, 0)]:
#         print("You win!")
#
#     elif houses[index(-1, 0)] > houses[index(-1, 1)]:
#         print("You lose!")
#
#     elif houses[index(-1, 0)] == houses[index(-1, 1)]:
#         print("Tie!")

def main(stdscr):
    # houses = [
    #     1, 2, 3, 4, 5, 4,
    #     0,
    #     0, 0, 1, 4, 0, 0,
    #     9,
    # ]
    houses = ([4] * board_size + [0]) * 2
    choice = 0

    # while check_empty(houses) == 'N':
    while True:
        print_board(stdscr, houses, choice)
        pressed = stdscr.getch()
        match chr(pressed):
            case 'h' | 'j' | 'a':
                choice = (choice - 1) % board_size
                continue
            case 'l' | 'd':
                choice = (choice + 1) % board_size
                continue
            case '\n':
                move(houses, index(choice, 1))
            case 'q':
                break
        stdscr.refresh()

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    main(stdscr)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
