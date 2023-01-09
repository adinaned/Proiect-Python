import mancala_controller as ctrl
import os
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
FONT = pygame.font.Font('EB Garamond.ttf', 25, bold = False)

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 620
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SCORE_IMG_WIDTH, SCORE_IMG_HEIGHT = 100, 50
SCORE_IMG_X_POS_LIST, SCORE_IMG_Y_POS_LIST = [[] for _ in range(2)],  [[] for _ in range(2)]
TOTAL_SCORE_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "total_score.png")).convert_alpha(WINDOW),
    (SCORE_IMG_WIDTH, SCORE_IMG_HEIGHT))

CUP_IMG_WIDTH, CUP_IMG_HEIGHT = 120, 120
CUP_IMG_X_POS_LIST, CUP_IMG_Y_POS_LIST = [[] for _ in range(2)],  [[] for _ in range(2)]
CUP_SCORE_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "cup_score.png")).convert_alpha(WINDOW),
    (SCORE_IMG_WIDTH, SCORE_IMG_HEIGHT))

STORE_IMG_WIDTH, STORE_IMG_HEIGHT = 120, 275
STONE_IMG_WIDTH, STONE_IMG_HEIGHT = CUP_IMG_WIDTH / 3, CUP_IMG_HEIGHT / 4

CURRENT_TURN_IMG = pygame.image.load(os.path.join("images", "current_turn.png")).convert_alpha(WINDOW)
CURRENT_TURN_IMG_WIDTH, CURRENT_TURN_IMG_HEIGHT = CURRENT_TURN_IMG.get_width(), CURRENT_TURN_IMG.get_height()
CURRENT_TURN_IMG_X, CURRENT_TURN_IMG_Y = WINDOW_WIDTH / 2 - CURRENT_TURN_IMG_WIDTH / 2, CURRENT_TURN_IMG_HEIGHT / 2

BOARD_IMG = pygame.image.load(os.path.join("images", "board.png")).convert_alpha(WINDOW)
BOARD_IMG_WIDTH, BOARD_IMG_HEIGHT = BOARD_IMG.get_width(), BOARD_IMG.get_height()
BOARD_IMG_X, BOARD_IMG_Y = 0, WINDOW_HEIGHT / 2  - BOARD_IMG.get_height() / 2 - 10 + CURRENT_TURN_IMG.get_height()

def save_score_position(img_x, img_y, row_index):
    '''
    saves the x coordinate of a specific score image in a matrix 
    which containes only the x coordinates of each score image
    same goes for y
    '''

    SCORE_IMG_X_POS_LIST[row_index].append(img_x)
    SCORE_IMG_Y_POS_LIST[row_index].append(img_y)

def save_cup_position(img_x, img_y, row_index):
    '''
    saves the x coordinate of a specific cup image in a matrix 
    which containes only the x coordinates of each score image
    same goes for y
    the store images' coordinates are also included in the matrices 
    '''

    CUP_IMG_X_POS_LIST[row_index].append(img_x)
    CUP_IMG_Y_POS_LIST[row_index].append(img_y)
    
def initialize_elements_positions():
    '''
    computes the coordinates for all store, cup and score images
    the coordinates for each image are saved in a matrix by calling
    a function that passes the coordinates as parameters
    '''

    for row_index in range(0, 2):
        for column_index in range (0, 7):
            if row_index == 0:
                if column_index == 0:
                    save_cup_position(STORE_IMG_WIDTH * column_index + STORE_IMG_WIDTH / 5, 
                                    BOARD_IMG_HEIGHT / 2 - STORE_IMG_HEIGHT / 2,
                                    row_index)
                    save_score_position(CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + CUP_IMG_WIDTH / 5 * (column_index - 1),
                                    BOARD_IMG_Y -  SCORE_IMG_HEIGHT,
                                    row_index)
                else:
                    save_cup_position(CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1) - 10, 
                                    BOARD_IMG_HEIGHT / 2 - CUP_IMG_HEIGHT - CUP_IMG_HEIGHT / 6,
                                    row_index)
                    save_score_position(CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + CUP_IMG_WIDTH / 5 * (column_index - 1), 
                                    BOARD_IMG_Y - SCORE_IMG_HEIGHT,
                                    row_index)
            else:
                if column_index == 6:
                    save_cup_position(STORE_IMG_WIDTH * (column_index + 2) + STORE_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5, 
                                    BOARD_IMG_HEIGHT / 2 - STORE_IMG_HEIGHT / 2,
                                    row_index)
                    save_score_position(CUP_IMG_WIDTH * (column_index + 1) + CUP_IMG_WIDTH / 2 + CUP_IMG_WIDTH / 5 * (column_index - 1) + 30, 
                                    BOARD_IMG_HEIGHT + BOARD_IMG_Y,
                                    row_index)
                else:
                    save_cup_position(CUP_IMG_WIDTH * (column_index + 1) + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1) + 20, 
                                    BOARD_IMG_HEIGHT / 2 + CUP_IMG_HEIGHT / 6,
                                    row_index)
                    save_score_position(CUP_IMG_WIDTH * (column_index + 1) + CUP_IMG_WIDTH / 2 + CUP_IMG_WIDTH / 5 * (column_index - 1) + 30, 
                                    BOARD_IMG_HEIGHT + BOARD_IMG_Y,
                                    row_index)

def generate_stones_position():
    '''
    generates random coordinates for the initial state of the stones
    the states are saved in a 4-dimensional array stones_position[a][b][c][d]
    a - stone row
    b - stone column
    c - stone index from a cup
    d - x / y coordinates of the stone
    '''

    for row_index in (0, 1):
        stones_in_a_row_positions_list = list()
        for column_index in range(7):
            stones_in_cup = list()
            for number_of_stones in range(0, 4):
                if row_index == 0:
                    if(column_index != 0):
                        img_x = random.randint(int(CUP_IMG_X_POS_LIST[row_index][column_index] + 30), 
                                        int(CUP_IMG_X_POS_LIST[row_index][column_index] + CUP_IMG_WIDTH - 60))
                        img_y = random.randint(int(CUP_IMG_Y_POS_LIST[row_index][column_index - 1] + 20), 
                                    int(CUP_IMG_Y_POS_LIST[row_index][column_index - 1] + CUP_IMG_HEIGHT - 40))
                        stones_in_cup.append((img_x, img_y))

                if row_index == 1:
                    if(column_index != 6):
                        img_x = random.randint(int(CUP_IMG_X_POS_LIST[row_index][column_index] + 30), 
                                        int(CUP_IMG_X_POS_LIST[row_index][column_index] + CUP_IMG_WIDTH - 60))
                        img_y = random.randint(int(CUP_IMG_Y_POS_LIST[row_index][column_index] + 20), 
                                    int(CUP_IMG_Y_POS_LIST[row_index][column_index] + CUP_IMG_HEIGHT - 40))
                        stones_in_cup.append((img_x, img_y))

            stones_in_a_row_positions_list.append(stones_in_cup)
        ctrl.stones_positions_list.append(stones_in_a_row_positions_list)