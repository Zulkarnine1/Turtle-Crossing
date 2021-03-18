from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.dead = False
         self.shape("turtle")
         self.penup()
         self.color("black")
         self.setheading(90)
         self.goto(STARTING_POSITION[0],STARTING_POSITION[1])


     def move_forward(self):
         if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)



     def move_down(self):
         if self.ycor()>-280:
            self.forward(-1*MOVE_DISTANCE)

     def relocate(self):
         self.goto(STARTING_POSITION[0], STARTING_POSITION[1])



