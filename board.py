import pygame
from random import randint, choice
#from Noughts_and_Crosses import colours, screen_width, screen_height, screen


class Board:
    def __init__(self, screen, colours):
        self.board_values = [[['.', False], ['.', False], ['.', False]],
                             [['.', False], ['.', False], ['.', False]],
                             [['.', False], ['.', False], ['.', False]]]
        self.tile_size = 0  # adjust
        self.tile_buffer = 30  # adjust
        self.player_turn = 'O'  # TODO will be affected by last game, needs to be reset or tell game which player starting
        self.skip_computer_turn = False
        self.hard_turn_counter = 0
        self.players_moves = [(None, None)]

        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.colours = colours
        self.wait = False
        self.wait_timer = 0

        # fonts
        self.freesansbold_path = '/Users/towella/Documents/programming/python/Noughts_and_Crosses/freesansbold.ttf'
        self.icon_font = pygame.font.Font(self.freesansbold_path, 200)

        #  buttons
        # top
        self.topleftb = pygame.Rect(170, 10, 206, 206)
        self.topmidb = pygame.Rect(396, 10, 208, 206)
        self.toprightb = pygame.Rect(624, 10, 200, 206)
        # mid
        self.midleftb = pygame.Rect(170, 236, 206, 208)
        self.midmidb = pygame.Rect(396, 236, 208, 208)
        self.midrightb = pygame.Rect(624, 236, 200, 208)
        # bottom
        self.bottomleftb = pygame.Rect(170, 464, 206, 200)
        self.bottommidb = pygame.Rect(396, 464, 208, 200)
        self.bottomrightb = pygame.Rect(624, 464, 200, 200)

        # icon text
        self.icon_coords = [[[170, 10, False], [396, 10, False], [624, 10, False]],
                            [[170, 236, False], [396, 236, False], [624, 236, False]],
                            [[170, 464, False], [396, 464, False], [624, 464, False]]]  # TODO possibly do centering in update
        self.icon_text = self.icon_font.render(f'', True, colours['line'])

        # lines
        self.win_line = None
        self.lines = [pygame.Rect((self.screen_height // 3) - 10 + 160, 10, 20, 654),
        pygame.Rect((self.screen_height - self.screen_height // 3) - 10 + 160, 10, 20, 654),
        pygame.Rect(10 + 160, (self.screen_height // 3) - 10, 654, 20),
        pygame.Rect(10 + 160, (self.screen_height - self.screen_height // 3) - 10, 654, 20)]

    def clicked(self, mx, my):
        x = -1
        y = -1
        if self.wait is False:
            if self.topleftb.collidepoint((mx, my)):
                x = 0
                y = 0
            elif self.topmidb.collidepoint((mx, my)):
                x = 1
                y = 0
            elif self.toprightb.collidepoint((mx, my)):
                x = 2
                y = 0
            elif self.midleftb.collidepoint((mx, my)):
                y = 1
                x = 0
            elif self.midmidb.collidepoint((mx, my)):
                y = 1
                x = 1
            elif self.midrightb.collidepoint((mx, my)):
                y = 1
                x = 2
            elif self.bottomleftb.collidepoint((mx, my)):
                y = 2
                x = 0
            elif self.bottommidb.collidepoint((mx, my)):
                y = 2
                x = 1
            elif self.bottomrightb.collidepoint((mx, my)):
                y = 2
                x = 2

            # modifies board values
            if x != -1:
                if self.board_values[y][x][1] is False:
                    self.players_moves.append((y, x))
                    self.board_values[y][x][0] = self.player_turn
                    self.board_values[y][x][1] = True

                    # alternate player icon
                    if self.player_turn == 'X':
                        self.player_turn = 'O'
                    else:
                        self.player_turn = 'X'

        return self.score(x, y)

    def reset_board(self):
        self.board_values = [[['.', False], ['.', False], ['.', False]],
                             [['.', False], ['.', False], ['.', False]],
                             [['.', False], ['.', False], ['.', False]]]
        self.win_line = None
        self.wait_timer = 0
        self.wait = False
        self.skip_computer_turn = False
        self.board_full = False
        self.hard_turn_counter = 0
        self.players_moves = [(None, None)]

    def return_score(self, icon_type):
        self.skip_computer_turn = True
        if icon_type == 'X':
            return 1, 0
        else:
            return 0, 1

    def draw_win_line(self, direction, x=0, y=0):
        if direction == 'horizontal':
            self.win_line = pygame.Rect(x, y, 654, 20)
        elif direction == 'vertical':
            self.win_line = pygame.Rect(x, y, 20, 654)
        elif direction == 'diagonal negative':
            self.win_line = 'diagonal negative'
        elif direction == 'diagonal positive':
            self.win_line = 'diagonal positive'
        self.wait = True

    def score(self, x, y):
        X_score = 0
        O_score = 0
        self.board_full = True

        if x != -1:
            icon_type = self.board_values[y][x][0]

            # horizontal checks
            # if mid
            if x + 1 < len(self.board_values) and x - 1 >= 0:
                if self.board_values[y][x + 1][0] == icon_type and self.board_values[y][x - 1][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('horizontal', 170, (110 * (y * 2.08 + 1)))
                    return X_score, O_score
            # left
            elif x + 2 < len(self.board_values):
                if self.board_values[y][x + 1][0] == icon_type and self.board_values[y][x + 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('horizontal', 170, (110 * (y * 2.08 + 1)))
                    return X_score, O_score
            # right
            else:
                if self.board_values[y][x - 1][0] == icon_type and self.board_values[y][x - 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('horizontal', 170, (110 * (y * 2.08 + 1)))
                    return X_score, O_score


            # vertical checks
            if y + 1 < len(self.board_values) and y - 1 >= 0:
                if self.board_values[y + 1][x][0] == icon_type and self.board_values[y - 1][x][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('vertical', (265 * (x * 0.86 + 1)), 10)
                    return X_score, O_score
            # left
            elif y + 2 < len(self.board_values):
                if self.board_values[y + 1][x][0] == icon_type and self.board_values[y + 2][x][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('vertical', (265 * (x * 0.86 + 1)), 10)
                    return X_score, O_score
            # right
            else:
                if self.board_values[y - 1][x][0] == icon_type and self.board_values[y - 2][x][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('vertical', (265 * (x * 0.86 + 1)), 10)
                    return X_score, O_score


            # diagonal checks
            # middle
            if y + 1 < len(self.board_values) and x + 1 < len(self.board_values) and y - 1 >= 0 and x - 1 >= 0:
                if self.board_values[y + 1][x + 1][0] == icon_type and self.board_values[y - 1][x - 1][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal negative')
                    return X_score, O_score
            if y - 1 >= 0 and x + 1 < len(self.board_values) and y + 1 < len(self.board_values) and x - 1 >= 0:
                if self.board_values[y - 1][x + 1][0] == icon_type and self.board_values[y + 1][x - 1][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal positive')
                    return X_score, O_score
            # top
            # left
            elif y + 2 < len(self.board_values) and x + 2 < len(self.board_values):
                if self.board_values[y + 1][x + 1][0] == icon_type and self.board_values[y + 2][x + 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal negative')
                    return X_score, O_score
            # right
            elif y + 2 < len(self.board_values) and x - 2 >= 0:
                if self.board_values[y + 1][x - 1][0] == icon_type and self.board_values[y + 2][x - 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal positive')
                    return X_score, O_score
            # bottom
            # left
            elif y - 2 >= 0 and x + 2 < len(self.board_values):
                if self.board_values[y - 1][x + 1][0] == icon_type and self.board_values[y - 2][x + 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal positive')
                    return X_score, O_score

            # right
            elif y - 2 >= 0 and x - 2 >= 0:
                if self.board_values[y - 1][x - 1][0] == icon_type and self.board_values[y - 2][x - 2][0] == icon_type:
                    X_score, O_score = self.return_score(icon_type)
                    self.draw_win_line('diagonal negative')
                    return X_score, O_score

            # full board
            for row in self.board_values:
                for cell in row:
                    if cell[0] == '.':
                        self.board_full = False
            if self.board_full:
                self.wait = True
                return 0, 0

            #  click square without win
            return X_score, O_score
        # not click square
        return X_score, O_score

    def get_player_turn(self):
        return self.player_turn

    def computer_turn(self, mode):
        x = 0
        y = 0
        tally = 0
        tallyx = 0
        tallyo = 0
        icon = self.player_turn
        pygame.time.wait(500)
        # if mode is easy, pick a random position that is open to go
        # if the position isn't open, loop until an open position is chosen
        if mode == 'easy':
            x = randint(0, len(self.board_values) - 1)
            y = randint(0, len(self.board_values) - 1)
            if self.board_values[y][x][1] is False:
                self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            else:
                while self.board_values[y][x][1] is True:
                    x = randint(0, len(self.board_values) - 1)
                    y = randint(0, len(self.board_values) - 1)
                    if self.board_values[y][x][1] is False:
                        self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            # return and reset
            if self.player_turn == 'O':
                self.player_turn = 'X'
            else:
                self.player_turn = 'O'

            return self.score(x, y)

        # if mode is moderate check every open spot on the board
        if mode == 'moderate':
            for rowy in range(len(self.board_values)):
                for columnx in range(len(self.board_values)):
                    if self.board_values[rowy][columnx][1] is False:

                        tallyx, tallyo = 0, 0
                        # horizontal (if there are 2 of the same icon in the chosen cell's row, go in the chosen cell)
                        for cell in self.board_values[rowy]:
                            if cell[0] == 'X':
                                tallyx += 1
                            elif cell[0] == 'O':
                                tallyo += 1
                        if tallyx == 2 or tallyo == 2:
                            self.board_values[rowy][columnx][0] = self.player_turn
                            self.board_values[rowy][columnx][1] = True
                            x = columnx
                            y = rowy
                            # return and rest
                            if self.player_turn == 'O':
                                self.player_turn = 'X'
                            else:
                                self.player_turn = 'O'

                            return self.score(x, y)

                        tallyx, tallyo = 0, 0
                        # vertical (for every cell, if its in the chosen cell's column, add to tally, 2 of icon, go cell
                        for checky in range(len(self.board_values)):
                            for checkx in range(len(self.board_values)):
                                if checkx == columnx:
                                    if self.board_values[checky][checkx][0] == 'X':
                                        tallyx += 1
                                    elif self.board_values[checky][checkx][0] == 'O':
                                        tallyo += 1
                                    if tallyx == 2 or tallyo == 2:
                                        self.board_values[rowy][columnx][0] = self.player_turn
                                        self.board_values[rowy][columnx][1] = True
                                        x = columnx
                                        y = rowy
                                        # return and reset
                                        if self.player_turn == 'O':
                                            self.player_turn = 'X'
                                        else:
                                            self.player_turn = 'O'

                                        return self.score(x, y)

                        tallyx, tallyo = 0, 0
                        # diagonal negative
                        if (rowy, columnx) in [(0, 0), (1, 1), (2, 2)]:
                            for cell in [(0, 0), (1, 1), (2, 2)]:
                                if self.board_values[cell[0]][cell[1]][0] == 'X':
                                    tallyx += 1
                                elif self.board_values[cell[0]][cell[1]][0] == 'O':
                                    tallyo += 1
                                if tallyx == 2 or tallyo == 2:
                                    self.board_values[rowy][columnx][0] = self.player_turn
                                    self.board_values[rowy][columnx][1] = True
                                    x = columnx
                                    y = rowy
                                    # return and reset
                                    if self.player_turn == 'O':
                                        self.player_turn = 'X'
                                    else:
                                        self.player_turn = 'O'

                                    return self.score(x, y)

                        tallyx, tallyo = 0, 0
                        # diagonal positive
                        if (rowy, columnx) in [(0, 2), (1, 1), (2, 0)]:
                            for cell in [(0, 2), (1, 1), (2, 0)]:
                                if self.board_values[cell[0]][cell[1]][0] == 'X':
                                    tallyx += 1
                                elif self.board_values[cell[0]][cell[1]][0] == 'O':
                                    tallyo += 1
                                if tallyx == 2 or tallyo == 2:
                                    self.board_values[rowy][columnx][0] = self.player_turn
                                    self.board_values[rowy][columnx][1] = True
                                    x = columnx
                                    y = rowy
                                    # return and reset
                                    if self.player_turn == 'O':
                                        self.player_turn = 'X'
                                    else:
                                        self.player_turn = 'O'

                                    return self.score(x, y)

            # random go if no blocks or wins avaliable (same as easy)
            x = randint(0, len(self.board_values) - 1)
            y = randint(0, len(self.board_values) - 1)
            if self.board_values[y][x][1] is False:
                self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            else:
                while self.board_values[y][x][1] is True:
                    x = randint(0, len(self.board_values) - 1)
                    y = randint(0, len(self.board_values) - 1)
                    if self.board_values[y][x][1] is False:
                        self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            # return and reset
            if self.player_turn == 'O':
                self.player_turn = 'X'
            else:
                self.player_turn = 'O'

            return self.score(x, y)

        # if mode is hard do the same thing as moderate except check wins before blocks using player icon
        if mode == 'hard':
            self.hard_turn_counter += 1
            for i in range(2):
                for rowy in range(len(self.board_values)):
                    for columnx in range(len(self.board_values)):
                        if self.board_values[rowy][columnx][1] is False:

                            # -- special starting cases --

                            # if player goes in center on first move go in corner
                            # dont have to check if corner is filled because its computer's first turn after player
                            if self.hard_turn_counter == 1 and self.players_moves[-1] == (1, 1):
                                random_corner = choice([(0, 0), (0, 2), (2, 0), (2, 2)])
                                self.board_values[random_corner[0]][random_corner[1]][0] = self.player_turn
                                self.board_values[random_corner[0]][random_corner[1]][1] = True
                                x = random_corner[1]
                                y = random_corner[0]
                                # return and rest
                                if self.player_turn == 'O':
                                    self.player_turn = 'X'
                                else:
                                    self.player_turn = 'O'

                                return self.score(x, y)


                            # if player goes in corner or edge on first moev go in center
                            # dont have to check if corner is filled because its computer's first turn after player
                            elif self.hard_turn_counter == 1 and \
                                (self.players_moves[-1] in [(0, 2), (0, 0), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]):
                                self.board_values[1][1][0] = self.player_turn
                                self.board_values[1][1][1] = True
                                x = 1
                                y = 1
                                # return and rest
                                if self.player_turn == 'O':
                                    self.player_turn = 'X'
                                else:
                                    self.player_turn = 'O'

                                return self.score(x, y)

                            tally = 0
                            # horizontal (if there are 2 of the same icon in the chosen cell's row, go in the chosen cell)
                            for cell in self.board_values[rowy]:
                                if cell[0] == icon:
                                    tally += 1
                            if tally == 2:
                                self.board_values[rowy][columnx][0] = self.player_turn
                                self.board_values[rowy][columnx][1] = True
                                x = columnx
                                y = rowy
                                # return and rest
                                if self.player_turn == 'O':
                                    self.player_turn = 'X'
                                else:
                                    self.player_turn = 'O'

                                return self.score(x, y)

                            tally = 0
                            # vertical (for every cell, if its in the chosen cell's column, add to tally, 2 of icon, go cell
                            for checky in range(len(self.board_values)):
                                for checkx in range(len(self.board_values)):
                                    if checkx == columnx:
                                        if self.board_values[checky][checkx][0] == icon:
                                            tally += 1
                                        if tally == 2:
                                            self.board_values[rowy][columnx][0] = self.player_turn
                                            self.board_values[rowy][columnx][1] = True
                                            x = columnx
                                            y = rowy
                                            # return and reset
                                            if self.player_turn == 'O':
                                                self.player_turn = 'X'
                                            else:
                                                self.player_turn = 'O'

                                            return self.score(x, y)

                            tally = 0
                            # diagonal negative
                            if (rowy, columnx) in [(0, 0), (1, 1), (2, 2)]:
                                for cell in [(0, 0), (1, 1), (2, 2)]:
                                    if self.board_values[cell[0]][cell[1]][0] == icon:
                                        tally += 1
                                    if tally == 2:
                                        self.board_values[rowy][columnx][0] = self.player_turn
                                        self.board_values[rowy][columnx][1] = True
                                        x = columnx
                                        y = rowy
                                        # return and reset
                                        if self.player_turn == 'O':
                                            self.player_turn = 'X'
                                        else:
                                            self.player_turn = 'O'

                                        return self.score(x, y)

                            tally = 0
                            # diagonal positive
                            if (rowy, columnx) in [(0, 2), (1, 1), (2, 0)]:
                                for cell in [(0, 2), (1, 1), (2, 0)]:
                                    if self.board_values[cell[0]][cell[1]][0] == icon:
                                        tally += 1
                                    if tally == 2:
                                        self.board_values[rowy][columnx][0] = self.player_turn
                                        self.board_values[rowy][columnx][1] = True
                                        x = columnx
                                        y = rowy
                                        # return and reset
                                        if self.player_turn == 'O':
                                            self.player_turn = 'X'
                                        else:
                                            self.player_turn = 'O'

                                        return self.score(x, y)

                if icon == 'X':
                    icon = 'O'
                else:
                    icon = 'X'

            # random go if no blocks or wins avaliable (same as easy)
            x = randint(0, len(self.board_values) - 1)
            y = randint(0, len(self.board_values) - 1)
            if self.board_values[y][x][1] is False:
                self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            else:
                while self.board_values[y][x][1] is True:
                    x = randint(0, len(self.board_values) - 1)
                    y = randint(0, len(self.board_values) - 1)
                    if self.board_values[y][x][1] is False:
                        self.board_values[y][x][0] = self.player_turn
                self.board_values[y][x][1] = True
            # return and reset
            if self.player_turn == 'O':
                self.player_turn = 'X'
            else:
                self.player_turn = 'O'

            return self.score(x, y)

        return 0, 0

    def update(self):
        offsetx = 0
        offsety = 0

        # icons # TODO possibly do centering in update
        for y in range(len(self.board_values)):
            for x in range(len(self.board_values[y])):
                offsetx = 0
                offsety = 0
                if self.board_values[y][x][0] != '.':
                    if self.board_values[y][x][0] == 'X':
                        self.icon_text = self.icon_font.render(f'X', True, self.colours['redX'])
                        offsetx = 38
                        offsety = 25
                    elif self.board_values[y][x][0] == 'O':
                        self.icon_text = self.icon_font.render(f'O', True, self.colours['blueO'])
                        offsetx = 27
                        offsety = 20
                    self.screen.blit(self.icon_text, (self.icon_coords[y][x][0] + offsetx, self.icon_coords[y][x][1] + offsety))

        # lines
        for line in self.lines:
            pygame.draw.rect(self.screen, self.colours['line'], line)

        if self.win_line is not None:
            if self.win_line == 'diagonal negative':
                pygame.draw.line(self.screen, self.colours['win_line'], (200, 40), (810, 650), 30)
            elif self.win_line == 'diagonal positive':
                pygame.draw.line(self.screen, self.colours['win_line'], (810, 29), (200, 639), 30)
            else:
                pygame.draw.rect(self.screen, self.colours['win_line'], self.win_line)

        if self.wait:
            self.wait_timer += 1
            if self.wait_timer >= 60:
                self.reset_board()
