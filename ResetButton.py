from Button import Button
from Score import player_left, player_right


class ResetButton(Button):

    def reset(self):
        player_left.score = 0
        player_right.score = 0

    def onClick(self):
        #implementacja funkcji z Button
        self.reset()
