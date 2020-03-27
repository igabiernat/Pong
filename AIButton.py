from Button import Button
from Globals import Steering

class AIButton(Button):
    isPlayingwithAI = False
    text1 = "AI"
    text2 = "1v1"

    def __init__(self,text,x,y,width,height, paddle):
        Button.__init__(self,text,x,y,width,height)
        self.paddle = paddle

    def AI(self):
        self.isPlayingwithAI = True
        self.text = self.text2
        self.paddle.steering = Steering.AI

    def onClick(self):
        if not self.isPlayingwithAI:
            self.AI()
        else:
            self.normal()

    def normal(self):
        self.isPlayingwithAI = False
        self.text = self.text1
        self.paddle.steering = Steering.Mouse

