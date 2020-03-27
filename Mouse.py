import pygame


class Mouse:
    x = 0
    y = 0
    last_pos = None
    delta_pos = None

    @staticmethod
    def update():
        Mouse.x, Mouse.y = pygame.mouse.get_pos()   #zapis ruchu myszki

    @staticmethod
    def getDeltaPos():
        #obliczanie zmiany pozycji kursora
        if Mouse.last_pos is None:
            Mouse.last_pos = (Mouse.x, Mouse.y)
        delta_pos = (Mouse.x - Mouse.last_pos[0], Mouse.y - Mouse.last_pos[1])
        Mouse.last_pos = (Mouse.x, Mouse.y)
        return delta_pos
