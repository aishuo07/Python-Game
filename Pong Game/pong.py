import turtle
import winsound

# score


score_a = 0
score_b = 0

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pong By Aish")
wn.setup(width=800, height=600)
wn.tracer(0)
# Paddle 1


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle 2


paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(+350, 0)

# ball


ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = -.3
ball.dy = -.3


# paddle1 up
def paddle_a_up():
    y = paddle_a.ycor()
    paddle_a.sety(y + 20)

#paddle_a_down

def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y - 20)

#paddle_up

def paddle_b_up():
    y = paddle_b.ycor()
    paddle_b.sety(y + 20)

#paddle_down

def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y - 20)


# pen


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align='center', font=("Aria;", 24, "normal"))

# keyboard binding


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align='center', font=("Arial", 24, "normal"))
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align='center',
                  font=("Arial", 24, "normal"))
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)
    # paddle and ball bounce

    if ball.xcor() > 340 and ball.xcor() > 350 and ball.ycor() < paddle_b.ycor() + 50:
        if ball.ycor() > paddle_b.ycor() - 50:
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)
    if ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() < paddle_a.ycor() + 50:
        if ball.ycor() > paddle_a.ycor() - 50:
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)
