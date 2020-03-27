from Button import Button
from Paddle import *
from Mouse import Mouse

class PauseButton(Button):
    isPaused = False
    playText = 'Play'
    pauseText = 'Pause'

    def pause(self):
        self.temp_paddle_speed = paddle_right.aiSpeed #zapisanie prędkości przed pauzą
        self.isPaused = True
        self.temp_ball_speed = (ball.Vx, ball.Vy)
        self.text = self.playText
        ball.Vx = 0     #zatrzymanie piłki
        ball.Vy = 0
        paddle_left.speed = 0   #zatrzymanie paletek
        if paddle_right.steering == Steering.AI:
            paddle_right.aiSpeed = 0
            paddle_right.isPaused = True
        else:
            paddle_right.isPaused = True

    def onClick(self):
        #implementacja funkcji z Button
        if self.isPaused:
            self.resume()
        else:
            self.pause()

    def resume(self):
        #wznowienie gry - ruchu piłki i paletek
        self.isPaused = False
        self.text = self.pauseText
        ball.Vx = self.temp_ball_speed[0]
        ball.Vy = self.temp_ball_speed[1]
        paddle_left.speed = 15
        if paddle_right.steering == Steering.AI:
            paddle_right.aiSpeed = self.temp_paddle_speed
            paddle_right.isPaused = False
        else:
            paddle_right.isPaused = False
