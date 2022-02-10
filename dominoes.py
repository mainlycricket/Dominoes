import random

all_pieces = []
stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
status = None
result = None

# Preparing list of all pieces: [[0, 0], [0, 1]...[0, 6], [1, 1]...[1, 6], [2, 2]...[2, 6]...[6, 6]]
for i in range(0, 7):
    for j in range(i, 7):
        temp = [i, j]
        all_pieces.append(temp)


# function to pick the first domino snake: the maximum double
def set_snake_piece(piece_list):

    for check_piece in piece_list:

        if check_piece[0] == check_piece[1]:

            if len(domino_snake) > 0 and check_piece[0] > domino_snake[0][0]:
                domino_snake.clear()
                domino_snake.append(check_piece)

            elif len(domino_snake) == 0:
                domino_snake.append(check_piece)


# the loop runs until the domino snake as at least one piece
while len(domino_snake) < 1:

    # preparing computer pieces list
    computer_pieces.clear()
    while len(computer_pieces) < 7:
        temp_set = random.choice(all_pieces)
        if temp_set not in computer_pieces:
            computer_pieces.append(temp_set)

    # preparing player pieces list
    player_pieces.clear()
    while len(player_pieces) < 7:
        temp_set = random.choice(all_pieces)
        if temp_set not in computer_pieces and temp_set not in player_pieces:
            player_pieces.append(temp_set)

    # preparing stock pieces list
    stock_pieces.clear()
    for piece in all_pieces:
        if piece not in computer_pieces and piece not in player_pieces:
            stock_pieces.append(piece)

    set_snake_piece(computer_pieces)
    set_snake_piece(player_pieces)

# deciding who plays based based on the snake piece
if domino_snake[0] in computer_pieces:
    computer_pieces.remove(domino_snake[0])
    status = "It's your turn to make a move. Enter your command."

elif domino_snake[0] in player_pieces:
    player_pieces.remove(domino_snake[0])
    status = "Computer is about to make a move. Press Enter to continue..."


# the output function
def output():

    global status, computer_pieces, player_pieces, domino_snake

    for _ in range(70):
        print("=", end='')

    print("\nStock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))

    print()
    if len(domino_snake) > 6:   # printing domino snake differently if its length > 6
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


# counting the instances of each digit in computer pieces and domino snake: part of computer AI
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


# function to process the input by the user
def input_process():

    global status

    # if it is player's turn
    if status == "It's your turn to make a move. Enter your command.":

        flag = True

        while flag:

            try:
                player_input = int(input()) # reading piece number from player pieces

                if player_input in range(-1 * len(player_pieces), len(player_pieces) + 1):

                    # skipping the turn - against the player's wish
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

                        # if the player wants to add a piece at the start of the snake
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

                        # if the player wants to skip his turn and a piece from stock pieces
                        elif player_input == 0:

                            if stock_pieces:
                                extracted_piece = random.choice(stock_pieces)
                                stock_pieces.remove(extracted_piece)
                                player_pieces.append(extracted_piece)

                            flag = False
                            status = "Computer is about to make a move. Press Enter to continue..."

                        # if the player wants to add a piece at the end of the domino snake
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

    # computer's turn
    elif status == "Computer is about to make a move. Press Enter to continue...":

        player_input = input()  # player to hit enter

        num_score = count_instances()   

        computer_pieces_tuple = []
        computer_pieces_score = []

        for computer_piece in computer_pieces:  # finding score of each computer piece

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

        # forming a dictionary with computer pieces (key) and scores (value)
        piece_with_score = dict(zip(computer_pieces_tuple, computer_pieces_score))

        # sorting the dictionary based on the score
        sorted_computer_list = sorted(piece_with_score.items(), key=lambda t: t[1], reverse=True)

        # deciding computer's move based on sorted_computer_list
        for extracted_piece in sorted_computer_list:

            # checking if the piece can be added to the end of the domino snake
            if extracted_piece[0][0] == domino_snake[-1][1] or extracted_piece[0][1] == domino_snake[-1][1]:
                domino_snake.append(list(extracted_piece[0]))
                computer_pieces.remove(list(extracted_piece[0]))
                status = "It's your turn to make a move. Enter your command."
                break

            # checking if the piece can be added at the first index in the domino snake
            elif extracted_piece[0][0] == domino_snake[0][0] or extracted_piece[0][1] == domino_snake[0][0]:
                domino_snake.insert(0, list(extracted_piece[0]))
                computer_pieces.remove(list(extracted_piece[0]))
                status = "It's your turn to make a move. Enter your command."
                break

        # if no piece can be added to snake by computer -> using stock
        if status != "It's your turn to make a move. Enter your command.":
            if stock_pieces:
                extracted_piece = random.choice(stock_pieces)
                stock_pieces.remove(extracted_piece)
                computer_pieces.append(extracted_piece)
            status = "It's your turn to make a move. Enter your command."


# function to check the result
def check_result():

    global player_pieces, computer_pieces, domino_snake, status, result

    if not player_pieces:   # the player wins
        result = True
        status = "The game is over. You won!"

    elif not computer_pieces:   # the computer wins
        result = True
        status = "The game is over. The computer won!"

    elif len(stock_pieces) == 0:    # draw
        result = True
        status = "The game is over. It's a draw!"

    elif domino_snake[0][0] == domino_snake[-1][1]:    # draw

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


while result is None:   # performing tasks until a result is achieved
    input_process()
    check_result()
    output()
