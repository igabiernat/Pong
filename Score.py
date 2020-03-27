from IBehaviour import IBehaviour, AllBehaviours
from Globals import *


class Score(IBehaviour):
    def __init__(self, score, x, y):
        #konstruktor i dodanie obiektu do AllBehaviours
        self.score = score
        self.x = x
        self.y = y
        AllBehaviours.append(self)

    def write(self):
        #wyświetlanie wyniku
        myfont = pygame.font.SysFont('Cambria', 40)
        text_surface = myfont.render(str(self.score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        screen.blit(text_surface, text_rect)

    def action(self):
        #implementacja funkcji z IBehaviour
        self.write()


player_left = Score(0, width / 4, 10)
player_right = Score(0, width * 3 / 4, 10)