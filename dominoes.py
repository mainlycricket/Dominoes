import random

all_pieces = []
stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
status = None
result = None

for i in range(0, 7):
    for j in range(i, 7):
        temp = [i, j]
        all_pieces.append(temp)


def set_snake_piece(piece_list):

    for check_piece in piece_list:

        if check_piece[0] == check_piece[1]:

            if len(domino_snake) > 0 and check_piece[0] > domino_snake[0][0]:
                domino_snake.clear()
                domino_snake.append(check_piece)

            elif len(domino_snake) == 0:
                domino_snake.append(check_piece)


while len(domino_snake) < 1:

    computer_pieces.clear()
    while len(computer_pieces) < 7:
        temp_set = random.choice(all_pieces)
        if temp_set not in computer_pieces:
            computer_pieces.append(temp_set)

    player_pieces.clear()
    while len(player_pieces) < 7:
        temp_set = random.choice(all_pieces)
        if temp_set not in computer_pieces and temp_set not in player_pieces:
            player_pieces.append(temp_set)

    stock_pieces.clear()
    for piece in all_pieces:
        if piece not in computer_pieces and piece not in player_pieces:
            stock_pieces.append(piece)

    set_snake_piece(computer_pieces)
    set_snake_piece(player_pieces)

if domino_snake[0] in computer_pieces:
    computer_pieces.remove(domino_snake[0])
    status = "It's your turn to make a move. Enter your command."

elif domino_snake[0] in player_pieces:
    player_pieces.remove(domino_snake[0])
    status = "Computer is about to make a move. Press Enter to continue..."


def output():

    global status, computer_pieces, player_pieces, domino_snake

    for _ in range(70):
        print("=", end='')

    print("\nStock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))

    print()
    if len(domino_snake) > 6:
        print(domino_snake[0], domino_snake[1], domino_snake[2], sep='', end='')
        print("...", end='')
        print(domino_snake[-3], domino_snake[-2], domino_snake[-1], sep='')

    else:
        for snake in domino_snake:
            print(snake, end='')

    print("\nYour pieces:")

    for index in range(len(player_pieces)):
        print(str((index + 1)) + ":" + str(player_pieces[index]))

    print("\nStatus:", status)


output()


def count_instances():

    global computer_pieces, domino_snake

    score_list = [0, 0, 0, 0, 0, 0, 0, 0]
    calculate_score(computer_pieces, score_list)
    calculate_score(domino_snake, score_list)

    return score_list


def calculate_score(pieces_list, score_list):

    score_zero = score_one = score_two = score_three = score_four = score_five = score_six = 0

    for a_piece in pieces_list:

        if a_piece[0] == 0:
            score_zero += 1
        elif a_piece[0] == 1:
            score_one += 1
        elif a_piece[0] == 2:
            score_two += 1
        elif a_piece[0] == 3:
            score_three += 1
        elif a_piece[0] == 4:
            score_four += 1
        elif a_piece[0] == 5:
            score_five += 1
        elif a_piece[0] == 6:
            score_six += 1

        if a_piece[1] == 0:
            score_zero += 1
        elif a_piece[1] == 1:
            score_one += 1
        elif a_piece[1] == 2:
            score_two += 1
        elif a_piece[1] == 3:
            score_three += 1
        elif a_piece[1] == 4:
            score_four += 1
        elif a_piece[1] == 5:
            score_five += 1
        elif a_piece[1] == 6:
            score_six += 1

    score_list[0] += score_zero
    score_list[1] += score_one
    score_list[2] += score_two
    score_list[3] += score_three
    score_list[4] += score_four
    score_list[5] += score_five
    score_list[6] += score_six


def input_process():

    global status

    if status == "It's your turn to make a move. Enter your command.":

        flag = True

        while flag:

            try:
                player_input = int(input())

                if player_input in range(-1 * len(player_pieces), len(player_pieces) + 1):

                    if len(player_pieces) == 1 and player_input != 0 \
                            and player_pieces[0][0] != domino_snake[0][0] \
                            and player_pieces[0][1] != domino_snake[0][0] \
                            and player_pieces[0][0] != domino_snake[-1][1]\
                            and player_pieces[0][1] != domino_snake[-1][1]:

                        if stock_pieces:
                            extracted_piece = random.choice(stock_pieces)
                            stock_pieces.remove(extracted_piece)
                            player_pieces.append(extracted_piece)

                        flag = False
                        status = "Computer is about to make a move. Press Enter to continue..."

                    else:

                        if player_input < 0:

                            player_input *= -1
                            extracted_piece = player_pieces.pop(player_input - 1)

                            if extracted_piece[0] == domino_snake[0][0] or extracted_piece[1] == domino_snake[0][0]:
                                domino_snake.insert(0, extracted_piece)
                                flag = False
                                status = "Computer is about to make a move. Press Enter to continue..."

                            else:
                                player_pieces.insert(player_input - 1, extracted_piece)
                                print("Illegal move. Please try again.")

                        elif player_input == 0:

                            if stock_pieces:
                                extracted_piece = random.choice(stock_pieces)
                                stock_pieces.remove(extracted_piece)
                                player_pieces.append(extracted_piece)

                            flag = False
                            status = "Computer is about to make a move. Press Enter to continue..."

                        elif player_input > 0:

                            extracted_piece = player_pieces.pop(player_input - 1)

                            if extracted_piece[0] == domino_snake[-1][1] or extracted_piece[1] == domino_snake[-1][1]:
                                domino_snake.append(extracted_piece)
                                flag = False
                                status = "Computer is about to make a move. Press Enter to continue..."

                            else:
                                player_pieces.insert(player_input - 1, extracted_piece)
                                print("Illegal move. Please try again.")

                else:
                    print("Invalid input. Please try again.")

            except:
                print("Invalid input. Please try again.")

    elif status == "Computer is about to make a move. Press Enter to continue...":

        player_input = input()
        flag = True

        num_score = count_instances()

        computer_pieces_tuple = []
        computer_pieces_score = []

        for computer_piece in computer_pieces:

            temp_score = 0
            computer_pieces_tuple.append(tuple(computer_piece))

            if computer_piece[0] == 0:
                temp_score += num_score[0]
            elif computer_piece[0] == 1:
                temp_score += num_score[1]
            elif computer_piece[0] == 2:
                temp_score += num_score[2]
            elif computer_piece[0] == 3:
                temp_score += num_score[3]
            elif computer_piece[0] == 4:
                temp_score += num_score[4]
            elif computer_piece[0] == 5:
                temp_score += num_score[5]
            elif computer_piece[0] == 6:
                temp_score += num_score[6]

            if computer_piece[1] == 0:
                temp_score += num_score[0]
            elif computer_piece[1] == 1:
                temp_score += num_score[1]
            elif computer_piece[1] == 2:
                temp_score += num_score[2]
            elif computer_piece[1] == 3:
                temp_score += num_score[3]
            elif computer_piece[1] == 4:
                temp_score += num_score[4]
            elif computer_piece[1] == 5:
                temp_score += num_score[5]
            elif computer_piece[1] == 6:
                temp_score += num_score[6]

            computer_pieces_score.append(temp_score)

        piece_with_score = dict(zip(computer_pieces_tuple, computer_pieces_score))
        sorted_computer_list = sorted(piece_with_score.items(), key=lambda t: t[1], reverse=True)

        for extracted_piece in sorted_computer_list:

            if extracted_piece[0][0] == domino_snake[-1][1] or extracted_piece[0][1] == domino_snake[-1][1]:
                domino_snake.append(list(extracted_piece[0]))
                computer_pieces.remove(list(extracted_piece[0]))
                status = "It's your turn to make a move. Enter your command."
                break

            elif extracted_piece[0][0] == domino_snake[0][0] or extracted_piece[0][1] == domino_snake[0][0]:
                domino_snake.insert(0, list(extracted_piece[0]))
                computer_pieces.remove(list(extracted_piece[0]))
                status = "It's your turn to make a move. Enter your command."
                break

        if status != "It's your turn to make a move. Enter your command.":
            if stock_pieces:
                extracted_piece = random.choice(stock_pieces)
                stock_pieces.remove(extracted_piece)
                computer_pieces.append(extracted_piece)
            status = "It's your turn to make a move. Enter your command."


def check_result():

    global player_pieces, computer_pieces, domino_snake, status, result

    if not player_pieces:
        result = True
        status = "The game is over. You won!"

    elif not computer_pieces:
        result = True
        status = "The game is over. The computer won!"

    elif len(stock_pieces) == 0:
        result = True
        status = "The game is over. It's a draw!"

    elif domino_snake[0][0] == domino_snake[-1][1]:

        counter = 0
        first_last_num = domino_snake[0][0]

        for snake_piece in domino_snake:

            if snake_piece[0] == first_last_num:
                counter += 1

            if snake_piece[1] == first_last_num:
                counter += 1

        if counter == 8:
            result = True
            status = "The game is over. It's a draw!"


while result is None:
    input_process()
    check_result()
    output()
