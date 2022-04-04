from turtle import  Turtle
ALIGNMENT = "center"
FONT = ( "Courier", "24", "normal")
class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score is {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()


    def update_score (self):
        self.score += 1
        self.clear()
        self.write(f"Score is {self.score}",align=ALIGNMENT,font=FONT)

    def game_over (self) :
        self.goto(0,0)
        self.write("Game is Over!",align=ALIGNMENT,font=FONT)