
import  turtle
import random

score= 0
lives= 3

wn=turtle.Screen()
wn.title("falling Skies by @Shhimona")
wn.bgcolor('green')
wn.bgpic(r"C:\Users\Simon\Desktop\PyCarm\backgound.gif")
wn.setup(width=800, height=600)
wn.tracer(14)

wn.register_shape(r"C:\Users\Simon\Desktop\PyCarm\bibble.gif")
wn.register_shape(r"C:\Users\Simon\Desktop\PyCarm\food.gif")
wn.register_shape(r"C:\Users\Simon\Desktop\PyCarm\bad guy.gif")

#Add player
player= turtle.Turtle()
player.speed(4)
player.shape(r"C:\Users\Simon\Desktop\PyCarm\bibble.gif")
player.color('blue')
player.penup()
player.goto(0, -245)
player.direction="stop"

#Good guys list
Gplayers= []

#gOOD GUYS
for _ in range(20):
    Gplayer = turtle.Turtle()
    Gplayer.speed(0)
    Gplayer.shape(r"C:\Users\Simon\Desktop\PyCarm\food.gif")
    Gplayer.color("white")
    Gplayer.penup()
    Gplayer.goto(0 , 250)
    Gplayer.speed= random.randint(1, 4)
    Gplayers.append(Gplayer)

#Bad guys list
Bplayers= []

#bad GUYS
for _ in range(20):
    Bplayer = turtle.Turtle()
    Bplayer.speed(0)
    Bplayer.shape(r"C:\Users\Simon\Desktop\PyCarm\bad guy.gif")
    Bplayer.color("red")
    Bplayer.penup()
    Bplayer.goto(100 , 250)
    Bplayer.speed= random.randint(1, 4)
    Bplayers.append(Bplayer)

#pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write( "Score:{}   Lives:{}".format(score,lives ) , align="center", font=font)



#Function
def go_left():
    player.direction="left"

def go_right():
    player.direction="right"

#Keyboard controls
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Main game loop
while True:
    wn.update()

    #Move the player
    if player.direction =="left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)


    #Move the good guys
    for Gplayer in Gplayers:
        y = Gplayer.ycor()
        y -= Gplayer.speed
        Gplayer.sety(y)

        #If its off the screen
        if y <-300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            Gplayer.goto(x , y)

        #Check for a collision with the player
        if Gplayer.distance(player)< 22:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            Gplayer.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score:{}   Lives:{}".format(score, lives), align="center", font=font)

    #Move the bad guys
    for Bplayer in Bplayers:
        y = Bplayer.ycor()
        y -= Bplayer.speed
        Bplayer.sety(y)

        #If its off the screen
        if y <-300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            Bplayer.goto(x , y)

        #Check for a collision with the player
        if Bplayer.distance(player)< 22:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            Bplayer.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score:{}   Lives:{}".format(score, lives), align="center", font=font)

wn.mainloop()