
#########################################################################################################
# source page https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
#########################################################################################################

import pygame


class InputBox:
    def __init__(self, x, y, w, h, colours, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colours = colours
        self.color = self.colours['bg']
        self.default_text = text
        self.text = text
        self.freesansbold_path = '/Users/towella/Documents/programming/python/Noughts_and_Crosses/freesansbold.ttf'
        self.font = pygame.font.Font(self.freesansbold_path, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                self.text = ''
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.colours['blueO'] if self.active else self.colours['bg']
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.colours['bg'])
        # length cap
        if len(self.text) > 8:
            self.text = self.text[:-1]
            self.txt_surface = self.font.render(self.text, True, self.colours['bg'])

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
