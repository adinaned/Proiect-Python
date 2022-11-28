import pygame
import os

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 620
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Mancala")

BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "background.png")).convert_alpha(WINDOW), 
    (WINDOW_WIDTH, WINDOW_HEIGHT))

CUP_IMG_WIDTH, CUP_IMG_HEIGHT = 120, 120
STORE_IMG_WIDTH, STORE_IMG_HEIGHT = 120, 275

NEXT_TURN_IMG = pygame.image.load(os.path.join("Images", "next_turn.png")).convert_alpha(WINDOW)
NEXT_TURN_IMG_X, NEXT_TURN_IMG_Y = WINDOW_WIDTH / 2 - NEXT_TURN_IMG.get_width() / 2, NEXT_TURN_IMG.get_height() / 2

BOARD_IMG = pygame.image.load(os.path.join("Images", "board.png")).convert_alpha(WINDOW)
BOARD_IMG_WIDTH, BOARD_IMG_HEIGHT = BOARD_IMG.get_width(), BOARD_IMG.get_height()
BOARD_IMG_X, BOARD_IMG_Y = 0, WINDOW_HEIGHT / 2 - BOARD_IMG.get_height() / 2 - 10 + NEXT_TURN_IMG.get_height()

CUP_SCORE_IMG_WIDTH, CUP_SCORE_IMG_HEIGHT = 50, 50
CUP_SCORE_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "cup_score.png")).convert_alpha(WINDOW),
    (CUP_SCORE_IMG_WIDTH, CUP_SCORE_IMG_HEIGHT))

FPS = 60

def load_store_image(row_index, column_index):
    store_img_path = os.path.join("Images", "cup_" + str(row_index) + str(column_index) + ".png")
    store_img = pygame.transform.scale(
        pygame.image.load(store_img_path).convert_alpha(BOARD_IMG), 
        (STORE_IMG_WIDTH, STORE_IMG_HEIGHT))
    return store_img

def load_cup_image(row_index, column_index):
    cup_img_path = os.path.join("Images", "cup_" + str(row_index) + str(column_index) + ".png")
    cup_img = pygame.transform.scale(
        pygame.image.load(cup_img_path).convert_alpha(BOARD_IMG), 
        (CUP_IMG_WIDTH, CUP_IMG_HEIGHT))
    return cup_img

def place_cups_and_stores():
    for row_index in range(0, 2):
        for column_index in range (0, 8):
            if row_index == 1 and (column_index == 0 or column_index == 7):
                continue

            if row_index == 0:
                if column_index == 0:
                    store_img = load_store_image(row_index, column_index)
                    BOARD_IMG.blit(store_img, 
                        (STORE_IMG_WIDTH * column_index + STORE_IMG_WIDTH / 5, 
                        BOARD_IMG_HEIGHT / 2 - STORE_IMG_HEIGHT / 2))
                elif column_index == 7:
                    store_img = load_store_image(row_index, column_index)
                    BOARD_IMG.blit(store_img, 
                        (STORE_IMG_WIDTH * (column_index + 1) + STORE_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5, 
                        BOARD_IMG_HEIGHT / 2 - STORE_IMG_HEIGHT / 2))
                else:
                    cup_img = load_cup_image(row_index, column_index)
                    BOARD_IMG.blit(cup_img, 
                        (CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1), 
                        BOARD_IMG_HEIGHT / 2 - CUP_IMG_HEIGHT - CUP_IMG_HEIGHT / 6))
                    BOARD_IMG.blit(CUP_SCORE_IMG, 
                    (CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1), 
                    -CUP_IMG_HEIGHT))
            else:
                cup_img = load_cup_image(row_index, column_index)
                BOARD_IMG.blit(cup_img, 
                    (CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1), 
                    BOARD_IMG_HEIGHT / 2 + CUP_IMG_HEIGHT / 6))
                BOARD_IMG.blit(CUP_SCORE_IMG, 
                    (CUP_IMG_WIDTH * column_index + CUP_IMG_WIDTH / 2 + STORE_IMG_WIDTH / 5 * (column_index - 1), 
                    BOARD_IMG_HEIGHT *2  + CUP_SCORE_IMG_HEIGHT))

def draw_board():
    WINDOW.blit(BACKGROUND_IMG, (0, 0))
    WINDOW.blit(NEXT_TURN_IMG, (NEXT_TURN_IMG_X, NEXT_TURN_IMG_Y))
    WINDOW.blit(BOARD_IMG, (BOARD_IMG_X, BOARD_IMG_Y))

    place_cups_and_stores()
    pygame.display.update()

def validate_args(my_input):
    if len(str(my_input).split(" ")) != 1:
        raise Exception("Invalid number of arguments.")
    elif str(my_input) != "computer" and my_input != "player":
        raise Exception("This is not a valid option.")
    else:
        opponent_option = my_input

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_board()
    pygame.quit()

if __name__ == "__main__":
    my_input = input("Enter 'computer' or 'player' to choose your type of opponent: ")
    validate_args(my_input)
    main()

# castigatorul trebuie afisat ca output in consola sau trebuie sa fie afisat in fereastra cu jocul
# e ok sa folosesc pygame
# e ok sa lucrez numai cu imagini?
