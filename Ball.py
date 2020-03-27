from IBehaviour import IBehaviour, AllBehaviours
from Globals import *
from Score import player_right, player_left
import numpy


class Ball(IBehaviour):
    Vx = 5
    Vy = 5
    VDefault = 5

    def __init__(self, x, y, b_width, b_height, paddle_left, paddle_right): #konstruktor piłki, dodanie do AllBehaviours
        self.x = x
        self.y = y
        self.b_width = b_width
        self.b_height = b_height
        self.ball_rect = pygame.Rect(x, y, b_width, b_height)
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        AllBehaviours.append(self)

    def draw(self):
        pygame.draw.ellipse(screen, (255, 0, 0), self.ball_rect)    #rysowanie piłki

    lastCollision = False

    def move(self):
        #funkcja odpowiadająca za ruch piłki
        keys = pygame.key.get_pressed() #tablica z wciśniętymi przyciskami
        for i in range(pygame.K_1, pygame.K_9):
            #przyspieszenie piłki na przyciskach 1-9
            if keys[i]:
                self.Vx = numpy.sign(self.Vx)*(self.VDefault+(i-pygame.K_1))
                self.Vy = numpy.sign(self.Vy)*(self.VDefault+(i-pygame.K_1))

        self.ball_rect.move_ip(self.Vx, self.Vy) #ruch piłki
        if self.ball_rect.right >= width:   #sprawdzenie kolizji z prawą stroną ekranu
            self.ball_rect.x = width / 2    #ustawienie piłki na środku ekranu
            self.ball_rect.y = height / 2
            player_left.score += 1  #dodanie punkta dla gracza z lewej strony
        if self.ball_rect.left <= 0:    #sprawdzenie kolizji z lewą stroną ekranu
            self.ball_rect.x = width / 2    #ustawienie piłki na środku ekranu
            self.ball_rect.y = height / 2
            player_right.score += 1 #dodanie punkta dla gracza z prawej strony
        if self.ball_rect.bottom >= height: #odbicie przy kolizji z górą ekranu
            self.Vy *= -1
        if self.ball_rect.top <= 0: #odbicie przy kolizji z dołem ekranu
            self.Vy *= -1

        collisionLeft = self.ball_rect.colliderect(self.paddle_left.get_paddle_rect())  #wykrywanie kolizji z lewą paletką
        collisionRight = self.ball_rect.colliderect(self.paddle_right.get_paddle_rect())  #wykrywanie kolizji z prawą paletką

        if not self.lastCollision and (collisionLeft or collisionRight):
            #warunek potrzebny do prawidłowego odbijania się piłki
            self.Vx *= -1
            self.lastCollision = True
        if not collisionLeft and not collisionRight:
            self.lastCollision = False
        print(self.Vx)

    def action(self):
        #implementowanie funkcji z IBehaviour
        self.draw()
        self.move()

