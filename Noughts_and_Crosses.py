import pygame, sys, random
from board import Board
from text_box import InputBox

# General setup
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
game_speed = 60
freesansbold_path = '/Users/towella/Documents/programming/python/Noughts_and_Crosses/freesansbold.ttf'

# options
beatable = True
player1_name = 'player 1'
player2_name = 'player 2'
computer_player_turn = 'X'

# Screen Setup
screen_width = 1000  # 980
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE, vsync=True)
pygame.display.set_caption('Noughts and Crosses -- Main Menu -- Andrew Towell')

# Game Rectangles
# board lines

# Colours
colours_1 = {'line': (73, 88, 103), 'bg': (189, 213, 234),
           'blueO': (87, 115, 153), 'redX': (254, 95, 85),
           'highlight': (247, 247, 255), 'win_line': (93, 112, 131)}

colours_2 = {'line': (123, 30, 122), 'bg': (12, 10, 62),
           'blueO': (68, 143, 163), 'redX': (179, 63, 98),
           'highlight': (243, 198, 119), 'win_line': (243, 198, 119)}

colours_3 = {'line': (48, 99, 142), 'bg': (43, 45, 66),
           'blueO': (237, 174, 73), 'redX': (209, 73, 91),
           'highlight': (237, 242, 244), 'win_line': (0, 121, 140)}

colours = colours_3

# fonts
options_font_icon = pygame.font.Font(freesansbold_path, 100)
game_font_icon = pygame.font.Font(freesansbold_path, 60)
game_font_large = pygame.font.Font(freesansbold_path, 42)
game_font_normal = pygame.font.Font(freesansbold_path, 32)
game_font_small = pygame.font.Font(freesansbold_path, 22)


def main_menu():
    click = False

    while True:
        screen.fill(colours['bg'])
        # titles and general text
        main_menu_title = game_font_large.render(f'Noughts and Crosses -- Main Menu', True, colours['line'])
        screen.blit(main_menu_title, (130, 100))
        #controls_text = game_font_small.render(f'Controls: up = w/arrow up, down = s/arrow down, pause = p, exit/quit = ,/esc ', True, colours['line'])
        #screen.blit(controls_text, (30, 630))

        # x and y mouse pos
        mx, my = pygame.mouse.get_pos()

        # button rect and draw
        button_1 = pygame.Rect(300, 200, 400, 50)
        button_2 = pygame.Rect(300, 300, 400, 50)
        button_3 = pygame.Rect(300, 400, 400, 50)
        button_4 = pygame.Rect(300, 500, 400, 50)
        button_5 = pygame.Rect(850, 25, 120, 60)
        button_options = pygame.Rect(350, 600, 300, 50)
        pygame.draw.rect(screen, colours['line'], button_1)
        pygame.draw.rect(screen, colours['line'], button_2)
        pygame.draw.rect(screen, colours['line'], button_3)
        pygame.draw.rect(screen, colours['line'], button_4)
        pygame.draw.rect(screen, colours['line'], button_5)
        pygame.draw.rect(screen, colours['line'], button_options)
        # button text and draw
        b1_text = game_font_normal.render(f'Computer - Easy', True, colours['bg'])
        b1_icon = game_font_large.render(f'X', True, colours['redX'])
        screen.blit(b1_text, (360, 210))
        b2_text = game_font_normal.render(f'Computer - Normal', True, colours['bg'])
        b2_icon = game_font_large.render(f'O', True, colours['blueO'])
        screen.blit(b2_text, (345, 310))
        b3_text = game_font_normal.render(f'Computer - Hard', True, colours['bg'])
        b3_icon = game_font_large.render(f'X', True, colours['redX'])
        screen.blit(b3_text, (360, 410))
        b4_text = game_font_normal.render(f'Multiplayer', True, colours['bg'])
        b4_icon = game_font_large.render(f'O', True, colours['blueO'])
        screen.blit(b4_text, (410, 510))
        b5_text = game_font_normal.render(f'Quit', True, colours['bg'])
        screen.blit(b5_text, (873, 40))
        boption_text = game_font_normal.render(f'Options', True, colours['bg'])
        boption_icon = game_font_large.render(f'X', True, colours['redX'])
        screen.blit(boption_text, (435, 610))

        # if mouse touches buttons
        if button_1.collidepoint((mx, my)):
            screen.blit(b1_icon, (310, 208))
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Easy -- Andrew Towell')
                game(colours, 'easy')
        elif button_2.collidepoint((mx, my)):
            screen.blit(b2_icon, (310, 308))
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Normal -- Andrew Towell')
                game(colours, 'moderate')
        elif button_3.collidepoint((mx, my)):
            screen.blit(b3_icon, (310, 408))
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Hard -- Andrew Towell')
                game(colours, 'hard')
        elif button_4.collidepoint((mx, my)):
            screen.blit(b4_icon, (310, 508))
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Multiplayer -- Andrew Towell')
                game(colours, 'multi')
        elif button_5.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        elif button_options.collidepoint((mx, my)):
            screen.blit(boption_icon, (360, 608))
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Options -- Andrew Towell')
                options_screen()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_COMMA or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(game_speed)


def game(colours, mode):
    global player1_name, player2_name

    board = Board(screen, colours)
    # score
    player1_score = 0
    player2_score = 0
    X_score = 0
    O_score = 0
    player_turn = 'O'
    click = False


    running = True
    while running:

        # x and y mouse pos
        mx, my = pygame.mouse.get_pos()

        # current player's turn
        player_turn = board.get_player_turn()

        # Event Checks
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # player input
            if event.type == pygame.KEYDOWN:

                # debug keys
                if event.key == pygame.K_SLASH:
                    pass
                elif event.key == pygame.K_PERIOD:
                    pass
                elif event.key == pygame.K_p:
                    pass
                elif event.key == pygame.K_COMMA or event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.display.set_caption('Noughts and Crosses -- Main Menu -- Andrew Towell')
                elif event.key == pygame.K_u:
                    pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    X_score, O_score = board.clicked(mx, my)
                    if X_score or O_score:
                        player1_score += O_score
                        player2_score += X_score

        if mode != 'multi':
            if player_turn == computer_player_turn and not board.skip_computer_turn and not board.board_full:
                X_score, O_score = board.computer_turn(mode)
                if X_score or O_score:
                    player1_score += O_score
                    player2_score += X_score

        # Visuals
        screen.fill(colours['bg'])
        board.update()
        #pygame.draw.aaline(screen, colours['line'], (screen_width / 2, 0), (screen_width / 2, screen_height))
        o_player_icon = game_font_icon.render(f'O', True, colours['blueO'])
        x_player_icon = game_font_icon.render(f'X', True, colours['redX'])

        player1_label = game_font_normal.render(f'{player1_name}', True, colours['line'])
        player2_label = game_font_normal.render(f'{player2_name}', True, colours['line'])

        player1_score_text = game_font_normal.render(f'{player1_score}', True, colours['line'])
        player2_score_text = game_font_normal.render(f'{player2_score}', True, colours['line'])

        if player_turn == 'O':
            highlight_rect = pygame.Rect(16, 140, 150, 150)
            pygame.draw.rect(screen, colours['highlight'], highlight_rect)
        else:
            highlight_rect = pygame.Rect(828, 140, 150, 150)
            pygame.draw.rect(screen, colours['highlight'], highlight_rect)

        screen.blit(o_player_icon, (68, 150))
        screen.blit(x_player_icon, (882, 150))

        screen.blit(player1_label, (30, 200))
        screen.blit(player2_label, (840, 200))

        screen.blit(player1_score_text, (80, 250))
        screen.blit(player2_score_text, (894, 250))

        # buttons
        exit_button = pygame.Rect(890, 25, 80, 50)
        pygame.draw.rect(screen, colours['line'], exit_button)
        exit_text = game_font_small.render(f'Exit', True, colours['bg'])
        screen.blit(exit_text, (907, 40))

        # if mouse touches buttons
        if exit_button.collidepoint((mx, my)):
            if click:
                pygame.display.set_caption('Noughts and Crosses -- Main Menu -- Andrew Towell')
                running = False

        # Update
        pygame.display.flip()
        clock.tick(game_speed)


def options_screen():
    global player1_name, player2_name, colours, colours_1, colours_2, colours_3

    input_box1 = InputBox(600, 145, 200, 40, colours, player1_name)
    input_box2 = InputBox(600, 245, 200, 40, colours, player2_name)
    input_boxes = [input_box1, input_box2]
    click = False
    options = True

    while options:
        options_window = pygame.Rect(40, 40, screen_width / 1.09, screen_height / 1.14)
        pygame.draw.rect(screen, colours['line'], options_window)
        options_text = game_font_large.render(f'OPTIONS', True, colours['bg'])
        player1_text = game_font_normal.render(f'Player 1 Name ---------------', True, colours['bg'])
        player2_text = game_font_normal.render(f'Player 2 Name ---------------', True, colours['bg'])
        colour_text = game_font_normal.render(f'Colour Scheme', True, colours['bg'])
        screen.blit(options_text, (screen_width / 2 - 100, 80))
        screen.blit(player1_text, (170, 150))
        screen.blit(player2_text, (170, 250))
        screen.blit(colour_text, (screen_width / 2 - 115, 350))

        button_close = pygame.Rect(40, 40, 50, 50)
        #button_speedup = pygame.Rect(630, 170, 200, 100)
        pygame.draw.rect(screen, colours['line'], button_close)

        # colour scheme buttons
        button_colour1 = pygame.Rect(660, 440, 250, 150)
        button_colour2 = pygame.Rect(375, 440, 250, 150)
        button_colour3 = pygame.Rect(85, 440, 250, 150)
        pygame.draw.rect(screen, colours_1['bg'], button_colour1)
        pygame.draw.rect(screen, colours_2['bg'], button_colour2)
        pygame.draw.rect(screen, colours_3['bg'], button_colour3)

        # icons and secondary button layers
        button_colour1_textX = options_font_icon.render(f'X', True, colours_1['redX'])
        button_colour1_textO = options_font_icon.render(f'O', True, colours_1['blueO'])
        button_colour1_rect = pygame.Rect(670, 450, 230, 130)

        button_colour2_textX = options_font_icon.render(f'X', True, colours_2['redX'])
        button_colour2_textO = options_font_icon.render(f'O', True, colours_2['blueO'])
        button_colour2_rect = pygame.Rect(385, 450, 230, 130)

        button_colour3_textX = options_font_icon.render(f'X', True, colours_3['redX'])
        button_colour3_textO = options_font_icon.render(f'O', True, colours_3['blueO'])
        button_colour3_rect = pygame.Rect(95, 450, 230, 130)

        pygame.draw.rect(screen, colours_1['line'], button_colour1_rect)
        screen.blit(button_colour1_textX, (715, 470))
        screen.blit(button_colour1_textO, (775, 470))

        pygame.draw.rect(screen, colours_2['line'], button_colour2_rect)
        screen.blit(button_colour2_textX, (430, 470))
        screen.blit(button_colour2_textO, (490, 470))

        pygame.draw.rect(screen, colours_3['line'], button_colour3_rect)
        screen.blit(button_colour3_textX, (140, 470))
        screen.blit(button_colour3_textO, (200, 470))


        bclose_text = game_font_normal.render(f'X', True, colours['bg'])
        #bspeedup_text = game_font_normal.render(f'pass', True, colours['line'])
        #binfinite_text = game_font_normal.render(f'pass', True, colours['line'])
        screen.blit(bclose_text, (50, 50))
        #screen.blit(bspeedup_text, (690, 205))
        #screen.blit(binfinite_text, (690, 445))

        # x and y mouse pos
        mx, my = pygame.mouse.get_pos()

        if button_close.collidepoint((mx, my)):
            if click:
                options = False
                pygame.display.set_caption('Pong -- Main Menu -- Andrew Towell')
        elif button_colour1.collidepoint((mx, my)):
            if click:
                colours = colours_1
        elif button_colour2.collidepoint((mx, my)):
            if click:
                colours = colours_2
        elif button_colour3.collidepoint((mx, my)):
            if click:
                colours = colours_3

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_COMMA or event.key == pygame.K_ESCAPE:
                    options = False
                    pygame.display.set_caption('Pong -- Main Menu -- Andrew Towell')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            for box in input_boxes:
                box.handle_event(event)
                player1_name = input_boxes[0].text
                player2_name = input_boxes[1].text

        for box in input_boxes:
            box.update()
            box.draw(screen)
            if player1_name == '':
                player1_name = 'player 1'
            if player2_name == '':
                player2_name = 'player 2'

        pygame.display.update()
        clock.tick(game_speed)


main_menu()
