import random

def draw_game_board(game_board: list[str]) -> None:
    print(game_board[7] + "|" + game_board[8] + "|" + game_board[9])
    print("-+-+-")
    print(game_board[4] + "|" + game_board[5] + "|" + game_board[6])
    print("-+-+-")
    print(game_board[1] + "|" + game_board[2] + "|" + game_board[3])


def get_players():
    letter = ""

    while not (letter == "X" or letter == "O"):
        letter = input("Chces X nebo O?\n").upper()

    if letter == "X":
        return "X", "O"

    return "O", "X"


def get_starting_player():
    if random.randint(0, 1) == 0:
        return "computer"

    return "player"


# 7  8  9
# 4  5  6
# 1  2  3


def is_winner(game_board: list[str], player_mark: str) -> bool:
    return (
            (game_board[7] == player_mark and game_board[8] == player_mark and game_board[9] == player_mark) or
            (game_board[4] == player_mark and game_board[5] == player_mark and game_board[6] == player_mark) or
            (game_board[1] == player_mark and game_board[2] == player_mark and game_board[3] == player_mark) or
            (game_board[7] == player_mark and game_board[4] == player_mark and game_board[1] == player_mark) or
            (game_board[8] == player_mark and game_board[5] == player_mark and game_board[2] == player_mark) or
            (game_board[9] == player_mark and game_board[6] == player_mark and game_board[3] == player_mark) or
            (game_board[7] == player_mark and game_board[5] == player_mark and game_board[3] == player_mark) or
            (game_board[9] == player_mark and game_board[5] == player_mark and game_board[1] == player_mark)
    )


def is_cell_empty(game_board: list[str], position: int) -> bool:
    return game_board[position] == " "


def get_player_move(game_board: list[str]) -> int:
    position = -1
    # available_moves = range(1, 10)
    game_board_copy = game_board[1:]
    available_moves = []

    for index, item in enumerate(game_board_copy, start=1):
        if item == " ":
            available_moves.append(index)

    # info_string = f"Vyber is z poli - {', '.join(map(lambda letter: str(letter), available_moves))}"
    info_string = f"Vyber si z poli - {', '.join(map(str, available_moves))}"

    while position not in available_moves:
        try:
            position = int(input(info_string + "\n"))
        except ValueError:
            print(info_string)

    return position


def get_next_winning_position(game_board: list[str], player_mark: str) -> int:
    for index in range(1, 10):
        game_board_copy = game_board[:]
        if is_cell_empty(game_board, index):
            game_board_copy[index] = player_mark
            if is_winner(game_board_copy, player_mark):
                return index

    return -1


def get_remaining_random_position(game_board: list[str], moves: list[int]) -> int:
    available_moves = []

    for move in moves:
        if game_board[move] == " ":
            available_moves.append(move)

    # for index, item in enumerate(game_board, start=1):
    #     if item == " ":
    #         available_moves.append(index)

    if len(available_moves) > 0:
        return random.choice(available_moves)

    return -1


def get_computer_move(game_board: list[str], computer_mark: str) -> int:
    player_mark = "O" if computer_mark == "X" else "X"

    position = get_next_winning_position(game_board, computer_mark)

    if position != -1:
        return position

    position = get_next_winning_position(game_board, player_mark)

    if position != -1:
        return position

    # 7  8  9
    # 4  5  6
    # 1  2  3

    position = get_remaining_random_position(game_board, [1, 3, 7, 9])

    if position != -1:
        return position

    if is_cell_empty(game_board, 5):
        return 5

    return get_remaining_random_position(game_board, [2, 4, 6, 8])

    # for index in range(1, 10):  # tady zkoumame kdyz by komp nekam zahral, jestli by to vyhrani tah
    #     game_board_copy = game_board[:]
    #     if is_cell_empty(game_board, index):
    #         game_board_copy[index] = computer_mark
    #         if is_winner(game_board_copy, computer_mark):
    #             return index
    #
    # for index in range(1, 10):
    #     game_board_copy = game_board[:]
    #     if is_cell_empty(game_board, index):
    #         game_board_copy[index] = player_mark
    #         if is_winner(game_board_copy, player_mark):
    #             return index


while True:
    game_board: list[str] = [" "] * 10  # ["", "", "", "", "", "", "", "", "", ""]
    # game_board: list[str] = ["", "O", "O", "X", "X", "X", "O", "O", "X", " "]
    player_mark, computer_mark = get_players()
    # current_player = get_starting_player()
    current_player = "player"
    print(f"Tedka zacina {current_player}")

    # starting_mark = player_mark if starting_player == "player" else computer_mark
    #
    # game_board[7] = starting_mark
    # game_board[8] = starting_mark

    is_running = True

    while is_running:
        draw_game_board(game_board)

        if current_player == "player":
            position = get_player_move(game_board)
            game_board[position] = player_mark

            if is_winner(game_board, player_mark):
                print("Vyhral si")
                is_running = False
            # else:
            #     empty = False
            #
            #     for item in game_board:
            #         if item == " ":
            #             empty = True
            #
            #     if not empty:
            #         print("Konec hry - remiza")
            #         is_running = False
            #     else:
            #         current_player = "computer"
        else:  # tady budeme resit kompa
            position = get_computer_move(game_board, computer_mark)
            game_board[position] = computer_mark

            if is_winner(game_board, computer_mark):
                print("Prohral si, pocitac vyhral!")
                is_running = False
            # else:

        if is_running:
            empty = False

            for item in game_board[1:]:
                if item == " ":
                    empty = True

            if not empty:
                print("Konec hry - remiza")
                is_running = False
            else:
                current_player = "computer" if current_player == "player" else "player"
    #
    #
    # draw_game_board(game_board)
    #
    #     position = get_player_move(game_board)
    #     game_board[position] = player_mark
    #
    #     if is_winner(game_board, player_mark):
    #         print("Vyhral si")
    #         is_running = False
    #     else:
    #         empty = False
    #
    #         for item in game_board:
    #             if item == " ":
    #                 empty = True
    #
    #         if not empty:
    #             print("Konec hry - remiza")
    #             is_running = False
    #
    #     draw_game_board(game_board)

    if not input("Chces hrat znovu?\n").lower().startswith("a"):
        break
