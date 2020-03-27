import pygame
from IBehaviour import IBehaviour, AllBehaviours
from Mouse import Mouse
from Globals import screen


class Button(IBehaviour):
    button_surface = None

    def __init__(self, text, x, y, width, height):
        #konstruktor przycisku i dodanie go do IBehaviour
        self.button_surface = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        AllBehaviours.append(self)

    def draw(self):
        #rysowanie przycisku
        myfont = pygame.font.SysFont('Cambria', 25)
        pygame.draw.rect(screen, (10, 245, 20), self.button_surface)
        text_surface = myfont.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, self.button_surface)

    def onClick(self):
        #deklaracja funkcji, która będzie implementowana w konkretnych przyciskach
        pass

    last_button_pressed = 0

    def isClicked(self):
        #funkcja sprawdzająca czy przycisk został wciśnięty
        flag = False
        click = pygame.mouse.get_pressed()
        if self.x < Mouse.x < self.x + self.width and self.y < Mouse.y < self.y + self.height:
            if self.last_button_pressed == 0 and click[0] == 1:
                flag = True
        self.last_button_pressed = click[0]
        return flag

    def action(self):
        #implementacja funkcji z IBehaviour
        self.draw()
        if self.isClicked():
            self.onClick()
