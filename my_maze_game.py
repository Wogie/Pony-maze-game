import turtle
import random
import math

# Making the screen
screen = turtle.Screen()
screen.delay(0)
screen.bgpic('pics/RAL3S2U.gif')
screen.title("Save starving bony Pony from the hungry Domokun")
screen.setup(700, 700)

# Images
pony_image = "pics/pony-icon.gif"
domo_image = "pics/domokun.gif"
carrot_image = "pics/carrot.gif"
wall_image = 'pics/wall.gif'
screen.addshape(pony_image)
screen.addshape(domo_image)
screen.addshape(carrot_image)
screen.addshape(wall_image)


# Defining the classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(wall_image)
        self.color("black")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(0)
        self.hideturtle()


# Defining list to contain Domokun trail
trail = []


class Pony(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(pony_image)
        self.penup()
        self.speed(0)
        self.hp = 30

    # Define the function to move the Domokun
    # I do it here because I make it part of the pony movement

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        domokun.domo_move()

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        domokun.domo_move()

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        domokun.domo_move()

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        domokun.domo_move()

    def is_collision(self, target_object, just_coords=False):
        if just_coords:
            target_coords = target_object
        else:
            target_coords = (target_object.xcor(), target_object.ycor())

        a = self.xcor() - target_coords[0]
        b = self.ycor() - target_coords[1]
        c = math.sqrt(a ** 2 + b ** 2)

        if c < 5:
            return True
        else:
            return False


class Domokun(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(domo_image)
        self.penup()
        self.speed(0)
        self.hp = 20

    def domo_move(self):
        global prev, trail

        # Define the different moves
        up = (self.xcor(), self.ycor() + 24)
        down = (self.xcor(), self.ycor() - 24)
        left = (self.xcor() - 24, self.ycor())
        right = (self.xcor() + 24, self.ycor())

        # Checks whether the moves hit a wall
        options = []
        options.append(up) if up not in walls else None
        options.append(down) if down not in walls else None
        options.append(left) if left not in walls else None
        options.append(right) if right not in walls else None


        if self.is_close(pony):
            if pony.xcor() > self.xcor() and right in options:
                go = right
            elif pony.xcor() < self.xcor() and left in options:
                go = left
            elif pony.ycor() > self.ycor() and up in options:
                go = up
            elif pony.ycor() < self.ycor() and down in options:
                go = down
            else:
                go = random.choice(options)

        # Checks if this is the first move
        # If it is not, previous move has impact on decision
        elif prev is not None:
            random_roll = False
            up_chance = 0
            down_chance = 0
            left_chance = 0
            right_chance = 0
            if prev == 'up' and up in options:
                up_chance = 0.49
                down_chance = 0.01
                left_chance = 0.5 if left in options else 0
                right_chance = 0.5 if right in options else 0

            elif prev == 'down' and down in options:
                down_chance = 0.49
                up_chance = 0.01
                left_chance = 0.5 if left in options else 0
                right_chance = 0.5 if right in options else 0
            elif prev == 'left' and left in options:
                left_chance = 0.49
                right_chance = 0.01
                up_chance = 0.5 if up in options else 0
                down_chance = 0.5 if down in options else 0
            elif prev == 'right' and right in options:
                right_chance = 0.49
                left_chance = 0.01
                up_chance = 0.5 if up in options else 0
                down_chance = 0.5 if down in options else 0
            else:
                random_roll = True

            if random_roll:
                go = random.choice(options)
            else:
                chances = [up_chance, down_chance, left_chance, right_chance]
                go = random.choices([up, down, left, right], chances)[0]

        else:
            go = random.choice(options)

        if go == up:
            self.goto(up[0], up[1])
            prev = 'up'
        elif go == down:
            self.goto(down[0], down[1])
            prev = 'down'
        elif go == left:
            self.goto(left[0], left[1])
            prev = 'left'
        elif go == right:
            self.goto(right[0], right[1])
            prev = 'right'

        # Keep track of the trail
        trail.append((self.xcor(), self.ycor()))

    def is_close(self, target_object):
        target_coords = (target_object.xcor(), target_object.ycor())

        a = self.xcor() - target_coords[0]
        b = self.ycor() - target_coords[1]
        c = math.sqrt(a ** 2 + b ** 2)

        if c < 216:
            return True
        else:
            return False


class Domokun2(Domokun):
    def __init__(self):
        Domokun.__init__(self)

    def domo_move(self):
        global prev2

        # Define the different moves
        up = (self.xcor(), self.ycor() + 24)
        down = (self.xcor(), self.ycor() - 24)
        left = (self.xcor() - 24, self.ycor())
        right = (self.xcor() + 24, self.ycor())

        # Checks whether the moves hit a wall
        options = []
        options.append(up) if up not in walls else None
        options.append(down) if down not in walls else None
        options.append(left) if left not in walls else None
        options.append(right) if right not in walls else None

        # Checks if pony is nearby and moves towards it
        if self.is_close(pony):
            if pony.xcor() > self.xcor() and right in options:
                go = right
            elif pony.xcor() < self.xcor() and left in options:
                go = left
            elif pony.ycor() > self.ycor() and up in options:
                go = up
            elif pony.ycor() < self.ycor() and down in options:
                go = down
            else:
                go = random.choice(options)

        # Checks if this is the first move
        # If it is not, previous move has impact on decision
        elif prev2 is not None:
            random_roll = False
            up_chance = 0
            down_chance = 0
            left_chance = 0
            right_chance = 0
            if prev2 == 'up' and up in options:
                up_chance = 0.49
                down_chance = 0.01
                left_chance = 0.5 if left in options else 0
                right_chance = 0.5 if right in options else 0

            elif prev2 == 'down' and down in options:
                down_chance = 0.49
                up_chance = 0.01
                left_chance = 0.5 if left in options else 0
                right_chance = 0.5 if right in options else 0
            elif prev2 == 'left' and left in options:
                left_chance = 0.49
                right_chance = 0.01
                up_chance = 0.5 if up in options else 0
                down_chance = 0.5 if down in options else 0
            elif prev2 == 'right' and right in options:
                right_chance = 0.49
                left_chance = 0.01
                up_chance = 0.5 if up in options else 0
                down_chance = 0.5 if down in options else 0
            else:
                random_roll = True

            if random_roll:
                go = random.choice(options)
            else:
                chances = [up_chance, down_chance, left_chance, right_chance]
                go = random.choices([up, down, left, right], chances)[0]

        else:
            go = random.choice(options)

        if go == up:
            self.goto(up[0], up[1])
            prev2 = 'up'
        elif go == down:
            self.goto(down[0], down[1])
            prev2 = 'down'
        elif go == left:
            self.goto(left[0], left[1])
            prev2 = 'left'
        elif go == right:
            self.goto(right[0], right[1])
            prev2 = 'right'

        screen.ontimer(self.domo_move, random.randint(150, 300))



class Carrot(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(carrot_image)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.hp = 14

    def remove_from_maze(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Initialising classes
prev = None
prev2 = None
pen = Pen()
pony = Pony()
domokun = Domokun()
domokun2 = Domokun2()
enemies = [domokun, domokun2]

# Making out levels
levels = []
level1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXX            X',
    'XX         X XXXXXXXXXXXX',
    'XX XXXXXXX XXXXXXXXXXXXXX',
    'XX X     X             XX',
    'XX X XXXXXXXXXXXXXXXXX XX',
    'XX X X               X XX',
    'XX X X XXXXXXXX XXXX X XX',
    'XX X   X      X    XXX XX',
    'XX X XXX XXXXXXXXX X   XX',
    'XX X X X X       X X X XX',
    'XX X X X X XXXXX X X XXXX',
    'XX X X X X X   X X X X XX',
    'XX X X X X X   XXX X X XX',
    'XX X X X X XX XX   X X XX',
    'XX X X X X  X    X X X XX',
    'XX X X X XXXXXXXXX X X XX',
    'XX X X X           X X XX',
    'XX X X XXXXXXXXX XXX X XX',
    'XX X X         X     X XX',
    'XX X XXXXXXXXXXXXXXXXX XX',
    'XX X                   XX',
    'XX XXXXXXXXX XXXXXXXXXXXX',
    'XX         X             ',
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
]

level2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XDXXXXXXXXXX            X',
    'X     C      XXXXXXXXXX X',
    'XX XXXXXXX XXXXXXXXXXXXXX',
    'XX X                  CXX',
    'XX X XXXXXXXXXXXXXXXXX XX',
    'XX X X               X XX',
    'XX X X XXXXXXXX XXXX X XX',
    'XX X   X      X    X X XX',
    'XX X XXX XXXXXXXXX X   XX',
    'XX X X X X       X X X XX',
    'XX X X X X XXXXX X X X XX',
    'XX X X X X XP  X X X X XX',
    'XX X X X X X  CXXX X X XX',
    'XX X X X X XX XX   X X XX',
    'XX X X X X  X    X X X XX',
    'XX X X X XXXXXXXXX X X XX',
    'XX X X X           X X XX',
    'XXCX X XXXXXXXXX XXX X XX',
    'XX X                 X XX',
    'XX X XXXXXXXXXXXXXXXXX XX',
    'XX X         X         XX',
    'XX XXXXXXXXX XXXXXXXXXXXX',
    'XX    E    X        C   W',
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
]
levels.extend([level1, level2])

# Making the maze
walls = []
carrots = []
wincoords = (3000, 3000)
carrots_eaten = 0


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -280 + (x * 24)
            screen_y = 280 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                pony.goto(screen_x, screen_y)

            if character == "D":
                domokun.goto(screen_x, screen_y)

            if character == "E":
                domokun2.goto(screen_x, screen_y)

            if character == "C":
                carrots.append(Carrot(screen_x, screen_y))

            if character == 'W':
                global wincoords
                wincoords = (screen_x + 24, screen_y)

    pen.bk(1)


screen.tracer(0)
setup_maze(levels[1])
print("Pony has %i HP" % pony.hp)

# Key Bindings
screen.listen()
screen.onkey(pony.go_left, "Left")
screen.onkey(pony.go_right, "Right")
screen.onkey(pony.go_up, "Up")
screen.onkey(pony.go_down, "Down")

domokun2.domo_move()

die = False
while not die:

    for carrot in carrots:
        if pony.is_collision(carrot):
            carrot.remove_from_maze()
            pony.hp += carrot.hp
            print("Pony has %i HP" % pony.hp)
            carrots_eaten += 1

    for enemy in enemies:
        if pony.is_collision(enemy):
            pony.hp -= 50
            print("Pony has %i HP" % pony.hp)
            if pony.hp <= 0:
                print("You died!")
                die = True

    if pony.is_collision(wincoords, just_coords=True):
        if carrots_eaten >= 5:
            print("Hurray! You won!")
            die = True
        else:
            print("You have to eat all the carrots!!")

    screen.update()
screen.mainloop()
