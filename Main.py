import sys
import pygame
from Globals import screen, width, height
from IBehaviour import AllBehaviours
from PauseButton import PauseButton
from ResetButton import ResetButton
from Mouse import Mouse
from Paddle import paddle_right, ball
from AIButton import AIButton

#tworzenie przycisków
reset_button = ResetButton('Reset', (width / 2) - 40, 20, 80, 30)
pause_button = PauseButton('Pause', (width - 80), 20, 70, 40)
AI_button = AIButton('AI', 20, 20, 50, 30, paddle_right)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        Mouse.update()
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (width / 2, 20), (width / 2, height - 20))

        for behaviour in AllBehaviours:
            #wywołanie funkcji action dla każdego obiektu, który zostal dodany do AllBehaviours
            behaviour.action()
        pygame.display.update()

        FPS = 30
        fpsClock = pygame.time.Clock()
        fpsClock.tick(FPS)



if __name__== "__main__":
    main()