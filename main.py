import random as rd
import curses
import math as mt

board_size = 6
grid = {
    'height': 3,
    'width': 5,
    'message': 1,
}

caption = {
    0: 'It\'s your turn!',
    1: 'Invalid move!',
    2: 'Move again!',
    3: 'Capture! Press to continue.',
    4: 'You won!',
    5: 'You lost!',
    6: 'Tie!'
}

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
    return not player

def my_house(pos, i):
    return ((pos < 7) == (spot(pos + i) < 7))

def print_board(stdscr, houses, choice, message):
    # Horizontal lines
    stdscr.hline(0, 0, curses.ACS_BSBS, (board_size + 2) * (grid['width'] + 1))
    stdscr.hline(grid['height'] + 1, grid['width'] + 1, curses.ACS_BSBS, (board_size) * (grid['width'] + 1))
    stdscr.hline(grid['height'] * 2 + 2, 0, curses.ACS_BSBS, (board_size + 2) * (grid['width'] + 1))
    stdscr.hline(grid['height'] * 2 + 3 + grid['message'], 0, curses.ACS_BSBS, (board_size + 2) * (grid['width'] + 1))

    # Vertical lines
    stdscr.vline(1, 0, curses.ACS_SBSB, grid['height'] * 2 + 2 + grid['message'])
    for i in range(board_size):
        # stdscr.addch(0, (i + 1) * (grid['width'] + 1), curses.ACS_BSSS)
        stdscr.vline(1, (i + 1) * (grid['width'] + 1), curses.ACS_SBSB, grid['height'] * 2 + 1)
        # stdscr.addch(grid['height'] * 2 + 2, (i + 1) * (grid['width'] + 1), curses.ACS_SSBS)
    stdscr.vline(1, (board_size + 1) * (grid['width'] + 1), curses.ACS_SBSB, grid['height'] * 2 + 1)
    stdscr.vline(1, (board_size + 2) * (grid['width'] + 1), curses.ACS_SBSB, grid['height'] * 2 + 2 + grid['message'])

    # Intersection points
    ## Corners
    stdscr.addch(0, 0, curses.ACS_BSSB)
    stdscr.addch(0, (board_size + 2) * (grid['width'] + 1), curses.ACS_BBSS)
    stdscr.addch(grid['height'] * 2 + 3 + grid['message'], (board_size + 2) * (grid['width'] + 1), curses.ACS_SBBS)
    stdscr.addch(grid['height'] * 2 + 3 + grid['message'], 0, curses.ACS_SSBB)

    ## Tees
    stdscr.addch(0, (board_size + 1) * (grid['width'] + 1), curses.ACS_BSSS)
    stdscr.addch(grid['height'] * 2 + 2, (board_size + 1) * (grid['width'] + 1), curses.ACS_SSBS)
    stdscr.addch(grid['height'] + 1, (board_size + 1) * (grid['width'] + 1), curses.ACS_SBSS)
    stdscr.addch(grid['height'] + 1, grid['width'] + 1, curses.ACS_SSSB)
    for i in range(board_size):
        stdscr.addch(0, (i + 1) * (grid['width'] + 1), curses.ACS_BSSS)
        stdscr.addch(grid['height'] * 2 + 2, (i + 1) * (grid['width'] + 1), curses.ACS_SSBS)
    stdscr.addch(grid['height'] * 2 + 2, (board_size + 2) * (grid['width'] + 1), curses.ACS_SBSS)
    stdscr.addch(grid['height'] * 2 + 2, 0, curses.ACS_SSSB)

    ## Crosses
    for i in range(board_size - 1):
        stdscr.addch(grid['height'] + 1, (i + 2) * (grid['width'] + 1), curses.ACS_SSSS)

    # Values
    ## Mothers
    stdscr.addstr(grid['height'] + 1, 1, f'{houses[index(-1, 0)]:^{grid['width']}}')
    stdscr.addstr(grid['height'] + 1, (board_size + 1) * (grid['width'] + 1) + 1, f'{houses[index(-1, 1)]:^{grid['width']}}')

    ## Children
    for i in range(board_size):
        ### Top
        stdscr.addstr(mt.ceil(grid['height'] / 2), (i + 1) * (grid['width'] + 1) + 1, f'{houses[index(board_size - i - 1, 0)]:^{grid['width']}}')

        ### Bottom
        colour = 2 if i == choice else 1

        #### Fill
        for n in range(grid['height']):
            stdscr.hline((grid['height'] + 2) + n, (i + 1) * (grid['width'] + 1) + 1, ' ', (grid['width']), curses.color_pair(colour))

        stdscr.addstr(grid['height'] + 1 + mt.ceil(grid['height'] / 2), (i + 1) * (grid['width'] + 1) + 1, f'{houses[index(i, 1)]:^{grid['width']}}', curses.color_pair(colour))

    ## Message
    stdscr.addstr(grid['height'] * 2 + 2 + mt.ceil(grid['message'] / 2), 1, f'{caption[message]:^{(board_size + 2) * (grid['width'] + 1) - 1}}')


def move(houses, pos):
    if houses[pos] <= 0:
        return 1

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
            return 2

        if pieces == 0 and houses[spot(pos + i)] == 1 and my_house(pos, i) and houses[opposite(spot(pos + i))] > 0:
            # print("Capture!")
            piece_num = 1 + houses[opposite(spot(pos + i))]
            houses[opposite(spot(pos + i))] = 0
            houses[spot(pos + i)] = 0
            houses[index(-1, (0 if pos < 7 else 1))] += piece_num
            return 3

    return 0

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

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # houses = [
    #     0, 0, 0, 3, 0, 0,
    #     0,
    #     1, 0, 2, 0, 0, 0,
    #     9,
    # ]
    houses = ([4] * board_size + [0]) * 2
    (player, choice, message) = (True, 0, 0)

    while check_empty(houses) == 'N':
    # while True:
        print_board(stdscr, houses, choice, message)
        if not player:
            cell = rd.randint(0, board_size - 1)
            result = move(houses, index(cell, 0))
            match result:
                case 0 | 3:
                    player = swap_player(player)
                    message = 0
        else:
            pressed = stdscr.getch()
            match chr(pressed):
                case 'h' | 'j' | 'a':
                    choice = (choice - 1) % board_size
                    continue
                case 'l' | 'd':
                    choice = (choice + 1) % board_size
                    continue
                case '\n':
                    result = move(houses, index(choice, 1))
                    match result:
                        case 0:
                            player = swap_player(player)
                            message = 0
                        case 1:
                            message = 1
                        case 2:
                            message = 2
                        case 3:
                            message = 3
                            print_board(stdscr, houses, choice, message)
                            stdscr.getch()
                            player = swap_player(player)
                case 'q':
                    break
        stdscr.refresh()

    side = 0 if swap_player(check_empty(houses)) == 'B' else 1
    for i in range(board_size):
        houses[index(-1, side)] += houses[index(i, side)]
        houses[index(i, side)] = 0

    if houses[index(-1, 1)] > houses[index(-1, 0)]:
        message = 4
    elif houses[index(-1, 1)] > houses[index(-1, 0)]:
        message = 5
    else:
        message = 6
    print_board(stdscr, houses, -1, message)
    stdscr.getch()
    curses.echo()
    curses.nocbreak()
    curses.endwin()

if __name__ == '__main__':
    main()
