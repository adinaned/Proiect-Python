import mancala_initialization as init
import random

stones_positions_list = list()

def write_current_turn(opponent_type, turn, CURRENT_TURN_IMG):
    '''
    changes the turn with the other player
    chooses the message depending on the type of 
    opponent given as input and of whose turn it is
    writes on the screen whose turn it is
    '''
    
    if opponent_type == "computer":
        turn_message = ""
        if turn == 0:
            turn_message = "Computer's turn"
            turn = 0
        else:
            turn_message = "Your turn"
            turn = 1
    else:
        turn_message = ""
        if turn == 1:
            turn_message = "Player 2's turn"
            turn = 0
        else:
            turn_message = "Player 1's turn"
            turn = 1

    rended_turn_message = init.FONT.render(turn_message, True, init.BLACK)
    
    CURRENT_TURN_IMG.blit(rended_turn_message, 
            (init.CURRENT_TURN_IMG_WIDTH / 2 - rended_turn_message.get_width() / 2, 
            init.CURRENT_TURN_IMG_HEIGHT / 2 - rended_turn_message.get_height() / 2))

def place_score():
    '''
    draws the stones on the board game
    the x and y coordinates for each stone are taken from
    SCORE_IMG_X_POS_LIST and SCORE_IMG_Y_POS_LIST
    '''

    for row_index in range(2):
        for column_index in range(7):
            score_text = str(len(stones_positions_list[row_index][column_index]))

            score_text_rended = init.FONT.render(score_text, True, init.BLACK)
            score_tuple = (init.SCORE_IMG_X_POS_LIST[row_index][column_index] + init.SCORE_IMG_WIDTH / 2 - score_text_rended.get_width() / 2,
                        init.SCORE_IMG_Y_POS_LIST[row_index][column_index] + init.SCORE_IMG_HEIGHT / 2 - score_text_rended.get_height() / 2)
            init.WINDOW.blit(score_text_rended, score_tuple)

def check_mouse_click(click_position, turn):
    '''
    checks the mouse click to be inside a cup by 
    taking each cup coordinates
    skips over the stores if they were selected
    checks that a player clicked on one of his cups
    ignores if an empty cup was selected
    '''

    for row_index in range(len(init.CUP_IMG_X_POS_LIST)):
        for cup_index in range(len(init.CUP_IMG_X_POS_LIST[row_index])):
            min_x = init.CUP_IMG_X_POS_LIST[row_index][cup_index]
            max_x = init.CUP_IMG_X_POS_LIST[row_index][cup_index] + init.CUP_IMG_WIDTH
            min_y = init.CUP_IMG_Y_POS_LIST[row_index][cup_index]
            max_y = init.CUP_IMG_Y_POS_LIST[row_index][cup_index] + init.CUP_IMG_HEIGHT
            if (row_index == 0 and cup_index == 0) or (row_index == 1 and cup_index == 6):
                continue
            else:
                for _ in range(len(init.CUP_IMG_Y_POS_LIST[row_index])):
                    if (click_position[0] > min_x and click_position[0] < max_x and click_position[1] > min_y + 
                        init.BOARD_IMG_Y and click_position[1] < max_y + init.BOARD_IMG_Y):
                        if(row_index != turn):
                            print(f"These are the opponent's cups. It's player {turn + 1}'s turn.")
                            return
                        if(row_index == turn):
                            if len(stones_positions_list[row_index][cup_index]) > 0:
                                return move_stone(row_index, cup_index, turn)
                            return

def generate_computer_move():
    '''
    chooses a valid cup, randomly and stimulates the move
    '''

    column = random.randint(1,6)
    while len(stones_positions_list[0][column]) == 0:
        column = random.randint(1,6)

    return move_stone(0, column, 0)

def get_next_position(row_index, column_index):
    '''
    receives a row and column index and returns the indexes 
    for next position in counterclockwise rotation
    includes big cups
    '''

    if row_index == 0:
        if column_index == 0:
            return (1, 0)
        else:
            return (0, column_index - 1)
    else:
        if column_index == 6:
            return (0, 6)
        else:
            return (1, column_index + 1)

def move_stone(row, col, turn):
    '''
    updates the coordinates in stones_positions_list in
    order to execute the move
    describes what happens when a valid cup is clicked
    '''

    repeat_turn = 0
    new_row, new_col = row, col
    while (len(stones_positions_list[row][col])) > 0:
        (new_row, new_col) = get_next_position(new_row, new_col)
        if new_row == 0 and new_col == 0:
            if turn == 0:
                if (len(stones_positions_list[row][col])) == 1:
                    repeat_turn = 1
                
                img_x = random.randint(int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + 30), 
                                        int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + init.CUP_IMG_WIDTH - 60))
                img_y = random.randint(int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + 20), 
                                    int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + init.CUP_IMG_HEIGHT - 40))

                stones_positions_list[row][col][0] =  (img_x, img_y)               
                stones_positions_list[new_row][new_col].append(stones_positions_list[row][col][0])
                stones_positions_list[row][col].pop(0)

        elif new_row == 1 and new_col == 6:
            if turn == 1:
                if (len(stones_positions_list[row][col])) == 1:
                    repeat_turn = 1
                
                img_x = random.randint(int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + 30), 
                                        int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + init.CUP_IMG_WIDTH - 60))
                img_y = random.randint(int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + 20), 
                                    int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + init.CUP_IMG_HEIGHT - 40))

                stones_positions_list[row][col][0] =  (img_x, img_y)               
                stones_positions_list[new_row][new_col].append(stones_positions_list[row][col][0])
                stones_positions_list[row][col].pop(0)

        else:
            img_x = random.randint(int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + 30), 
                                    int(init.CUP_IMG_X_POS_LIST[new_row][new_col] + init.CUP_IMG_WIDTH - 60))
            img_y = random.randint(int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + 20), 
                                int(init.CUP_IMG_Y_POS_LIST[new_row][new_col] + init.CUP_IMG_HEIGHT - 40))

            stones_positions_list[row][col][0] =  (img_x, img_y)               
            stones_positions_list[new_row][new_col].append(stones_positions_list[row][col][0])
            stones_positions_list[row][col].pop(0)

    return repeat_turn

def check_final_state():
    '''
    returns 1 if the game got in a final state
    and 0 otherwise
    '''

    found_stone = 0
    for column_index in range(1, 7):
        if len(stones_positions_list[0][column_index]) > 0:
            found_stone = 1
            break
    if found_stone == 0:
        return 1

    found_stone = 0
    for column_index in range(6):
        if len(stones_positions_list[1][column_index]) > 0:
            found_stone = 1
            break
    if found_stone == 0:
        return 1

    return 0

def display_winner(opponent_type):
    '''
    computer who the winner is based on
    the number of points accumulated
    '''

    player_1_score = len(stones_positions_list[0][0])
    player_2_score = len(stones_positions_list[1][6])

    if opponent_type == "computer":
        if player_1_score > player_2_score:
            message = f"Computer: {player_1_score} stones. You 2: {player_2_score} stones.\nComputer won :("
        else:
            message = f"Computer: {player_1_score} stones. You 2: {player_2_score} stones.\nYou won!"
    else:
        if player_1_score > player_2_score:
            message  = f"Player 1: {player_1_score} stones. Player 2: {player_2_score} stones.\nPlayer 1 won!"
        else:
            message = f"Player 1: {player_1_score} stones. Player 2: {player_2_score} stones.\nPlayer 2 won!"
        
    print(message)
    exit()