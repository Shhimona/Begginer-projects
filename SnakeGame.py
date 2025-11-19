#SnakeGame

#Set the screen
import turtle
import time
import random

delay= 0.1

#Score
score=0
high_score=0


gm=turtle.Screen()
gm.title("Snake Game")
gm.bgcolor("Purple")
gm.setup(width=600 , height=600)
gm.tracer(0)    #This turns off the screen updates

#Snake head
Sh= turtle.Turtle()
Sh.speed(0)
Sh.shape("triangle")
Sh.color("Blue")
Sh.penup()
Sh.goto(0,0)
Sh.direction="stop"

#food
fs= turtle.Turtle()
fs.speed(0)
fs.shape("circle")
fs.color("black")
fs.penup()
fs.goto(0,100)

segments = []

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0   High Score:0" , align="center", font=("Courier", 24 , "normal"))



#Functions
def go_up():
    if Sh.direction !="down":
       Sh.direction = "up"

def go_down():
    if Sh.direction !="up":
       Sh.direction = "down"

def go_left():
    if Sh.direction !="right":
       Sh.direction = "left"

def go_right():
    if Sh.direction !="left":
       Sh.direction  = "right"

def move():
    if Sh.direction == "up":
           y = Sh.ycor()
           Sh.sety(y+ 20)


    if Sh.direction == "down":
        y = Sh.ycor()
        Sh.sety(y - 20)

    if Sh.direction == "left":
        x = Sh.xcor()
        Sh.setx(x - 20)

    if Sh.direction == "right":
        Sh.setx(Sh.xcor() + 20)

#keyboard bindings
gm.listen()
gm.onkeypress(go_up, "w")
gm.onkeypress(go_down, "s")
gm.onkeypress(go_right, "d")
gm.onkeypress(go_left, "a")

#main game loop (we do this because of line 9)
while True:
    gm.update()

    #Check for a collision with the border
    if Sh.xcor()>290 or Sh.xcor()<-290 or Sh.ycor()>290 or Sh.ycor()<-290:
        time.sleep(1)
        Sh.goto(0,0)
        Sh.direction="stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments
        segments.clear()

        #reset the score
        score=0

        #reset the delay
        delay=0.1

        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("Courie", 24, "normal"))

    #Check for a collision with the food
    if Sh.distance(fs) < 20:
         # Move the food random    Line 6
         y = random.randint(-290, 290)
         x = random.randint(-290,290)
         fs.goto(x,y)

         #Add segment
         New_segment= turtle.Turtle()
         New_segment.speed(0)
         New_segment.shape("circle")
         New_segment.color("black")
         New_segment.penup()
         segments.append(New_segment)

         #Shorten the delay
         delay-=0.001

         #Score increase
         score +=10

         if score > high_score:
            high_score = score


         pen.clear()
         pen.write("Score:{}  High Score:{}".format(score , high_score), align="center", font=("Courie", 24, "normal"))



    for index in range(len(segments)-1 , 0 , -1):
           x =segments[index -1].xcor()
           y =segments[index -1].ycor()
           segments[index].goto(x , y)

    if len(segments) > 0:
         x=Sh.xcor()
         y = Sh.ycor()
         segments[0].goto(x , y)


    move()

    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(Sh)< 20:
            time.sleep(1)
            Sh.goto(0,0)

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments list
            segments.clear()

    time.sleep(delay)


gm.mainloop()

