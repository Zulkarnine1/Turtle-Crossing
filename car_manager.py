from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_dis = STARTING_MOVE_DISTANCE
        self.make_car()

    def make_car(self):
        if(len(self.cars)<40):
            randomChoice = random.choice([0,1,3])
            if randomChoice == 1:
                car = Car()
                self.cars.append(car)

    def move_cars(self, player,score):
        for i in range(len(self.cars)):
            car = self.cars[i]
            if car.distance(player)<20:
                player.dead = True
                score.game_over()
            car.forward(self.move_dis)
            if car.xcor()<-300:
                random_y = random.randint(-240, 280)
                car.color(random.choice(COLORS))
                car.goto(300,random_y)

    def level_up(self):
        self.move_dis += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1,stretch_len=2)
        # self.hideturtle()
        random_y = random.randint(-280,280)
        self.goto(280,random_y)

    def delete_self(self):
        self.clear()


