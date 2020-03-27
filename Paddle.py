import pygame
from IBehaviour import IBehaviour, AllBehaviours
from Globals import *
from Mouse import Mouse
from Ball import Ball


class Paddle(IBehaviour):
    last_mouse_y = None
    speed = 15
    aiSpeed = 5
    isPaused = False

    def __init__(self, x, y, p_width, p_height, steering):
        #konstruktor paletki, dodanie do AllBehaviours
        self.x = x
        self.y = y
        self.p_width = p_width
        self.p_height = p_height
        self.steering = steering
        AllBehaviours.append(self)

    def get_paddle_rect(self):
        #tworzenie prostokąta
        paddle_rect = pygame.Rect(self.x, self.y, self.p_width, self.p_height)
        return paddle_rect

    def draw(self):
        #rysowanie prostokąta - paletki
        paddle_rect = self.get_paddle_rect()
        pygame.draw.rect(screen, (0, 0, 255), paddle_rect)

    def move(self):
        if self.steering == Steering.Arrows:    #sterowanie lewą paletką - strzałki
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and self.y < height - self.p_height:
                self.y += self.speed
            if keys[pygame.K_UP] and self.y > 0:
                self.y -= self.speed
        elif self.steering == Steering.Mouse:   #sterowanie prawą paletką - myszka
            if not self.isPaused:
                movement = Mouse.getDeltaPos()
                self.y += movement[1]
        elif self.steering == Steering.AI:      #przełączanie sterowania prawą paletką na AI
                self.play()

    def action(self):
        #implementowanie funkcji z IBehaviour
        self.draw()
        self.move()

    def play(self):
        #funkcja odpowiadajaca za grę z komputerem
        if not self.isPaused:
            if self.y >= 0 and self.y <= height - self.p_height:
                if ball.ball_rect.y < self.y + (self.p_height / 2):
                    self.aiSpeed -= 2.5   #odejmowanie szybkości kiedy piłka powyżej połowy wysokości paletki
                    self.y += self.aiSpeed
                else:
                    self.aiSpeed += 2.5   #dodawanie szybkości kiedy piłka poniżej połowy wysokości paletki
                    self.y += self.aiSpeed
            elif self.y < 0:       #zabezpieczenia przed znalezieniem się paletki poza ekranem gry
                self.y = 0
                self.aiSpeed = 0
            elif self.y > height - self.p_height:
                self.y = height - self.p_height
                self.aiSpeed = 0


paddle_left = Paddle(20, height / 2, 5, height/8, Steering.Arrows)
paddle_right = Paddle(width - 25, height / 2, 5, height/8, Steering.Mouse)

ball = Ball(width / 2, height / 2, width/80, width/80, paddle_left, paddle_right)
