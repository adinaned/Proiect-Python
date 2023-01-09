import mancala_initialization as init
import mancala_controller as ctrl
import mancala_UI as UI
import random
import pygame
import time

FPS = 30

def validate_input():
    '''
    validates the number of arguments given as input
    checks if the input is be a valid choice
    if not, the loop runs until the input is valid
    '''

    invalid = True
    my_input = input("\nEnter 'computer' or 'player' to choose your type of opponent: ")

    while invalid:
        if len(str(my_input).split(" ")) != 1:
            my_input = input("\nThe number of arguments is invalid.\nEnter 'computer' or 'player' to choose your type of opponent: ")
        elif str(my_input) != "computer" and my_input != "player":
            my_input = input("\nThis is not a valid option.\nEnter 'computer' or 'player' to choose your type of opponent: ")
        else:
            invalid = False
    return my_input

if __name__ == "__main__":
    '''
    calls all necessary functions to start the game
    manages the event loop
    '''

    opponent_type = validate_input()
    init.initialize_elements_positions()
    init.generate_stones_position()

    clock = pygame.time.Clock()
    run = True
    turn = random.randint(0, 2) % 2
    while run:
        clock.tick(FPS)

        turn = ctrl.manage_computer_game_mode(opponent_type, turn)
        UI.draw_board(opponent_type, turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn = ctrl.manage_2_players_mode(turn)

        if ctrl.check_final_state():
            ctrl.display_winner(opponent_type)   

    pygame.quit()