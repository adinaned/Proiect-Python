import mancala_initialization as init
import mancala_controller as ctrl
import pygame
import os

pygame.display.set_caption("Game of Mancala")

BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "background.png")).convert_alpha(init.WINDOW), 
    (init.WINDOW_WIDTH, init.WINDOW_HEIGHT))

def load_cup_and_store_image(row_index, column_index, BOARD_IMG, cup = True):
    '''
    loads the cup image for a specific row and column
    then it resizes it, adapts it to the board background and returns the image
    '''
    
    img_path = os.path.join("images", "cup_" + str(row_index) + str(column_index) + ".png")

    if cup == True:
        img_width, img_height = init.CUP_IMG_WIDTH, init.CUP_IMG_HEIGHT
    else:
        img_width, img_height = init.STORE_IMG_WIDTH, init.STORE_IMG_HEIGHT
        
    img = pygame.transform.scale(
        pygame.image.load(img_path).convert_alpha(BOARD_IMG), 
        (img_width, img_height))
    return img

def load_stone_image(index):
    '''
    loads the stone image
    then it resizes it and returns the images
    '''

    img_path = os.path.join("images", "stone_model_" + str(index) + ".png")
    
    img = pygame.transform.scale(
        pygame.image.load(img_path), 
        (init.STONE_IMG_WIDTH, init.STONE_IMG_HEIGHT))
    return img

def add_cups_and_scores_images(BOARD_IMG):
    '''
    all cups, stores and score images are added on the board
    '''

    for row_index in range(0, 2):
        for column_index in range (7):
            if (row_index == 0 and column_index == 0) or (row_index == 1 and column_index == 6):
                image = load_cup_and_store_image(row_index, column_index, BOARD_IMG, cup = False)
            else:
                image = load_cup_and_store_image(row_index, column_index, BOARD_IMG, cup = True)

            BOARD_IMG.blit(image, 
                        (init.CUP_IMG_X_POS_LIST[row_index][column_index], 
                        init.CUP_IMG_Y_POS_LIST[row_index][column_index]))
            init.WINDOW.blit(init.TOTAL_SCORE_IMG, 
                        (init.SCORE_IMG_X_POS_LIST[row_index][column_index], 
                        init.SCORE_IMG_Y_POS_LIST[row_index][column_index]))

def place_stones(BOARD_IMG):
    '''
    draws the stones on the board game
    the coordinates are takes from stones_positions_list
    '''

    for row_index in (0, 1):
        for column_index in range(7):
            for stone_index in range(len(ctrl.stones_positions_list[row_index][column_index])):
                BOARD_IMG.blit(load_stone_image(1),
                            (ctrl.stones_positions_list[row_index][column_index][stone_index][0], 
                            ctrl.stones_positions_list[row_index][column_index][stone_index][1]))

def draw_board(opponent_type, turn):
    '''
    calls all functions that draw elements
    draws the background image
    calls the place_score(), place_stone() and add_cups_and_scores_images()
    function to add all elements
    adds the current turn image
    '''

    init.WINDOW.blit(BACKGROUND_IMG, (0, 0))

    BOARD_IMG = pygame.image.load(os.path.join("Images", "board.png")).convert_alpha(init.WINDOW)
    add_cups_and_scores_images(BOARD_IMG)
    place_stones(BOARD_IMG)
    init.WINDOW.blit(BOARD_IMG, (init.BOARD_IMG_X, init.BOARD_IMG_Y))


    CURRENT_TURN_IMG = pygame.image.load(os.path.join("Images", "current_turn.png")).convert_alpha(init.WINDOW)
    ctrl.write_current_turn(opponent_type, turn, CURRENT_TURN_IMG)
    ctrl.place_score()

    init.WINDOW.blit(CURRENT_TURN_IMG, (init.CURRENT_TURN_IMG_X, init.CURRENT_TURN_IMG_Y))

    pygame.display.flip()