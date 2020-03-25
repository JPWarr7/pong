# Programmed by JPWarren
# Pong
import turtle

wn = turtle.Screen()
wn.title("Pong by JPWarren")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_l = 0
score_r = 0

# Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=6, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=6, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {}  Player 2: {}".format(score_l, score_r),  align="center", font=("Courier", 24, "normal"))

# FUNCTIONS
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Key Binds
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")

# Main Loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_l, score_r),  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_l, score_r),  align="center", font=("Courier", 24, "normal"))

    # Paddle Mechanics wih Ball
    if (340 < ball.xcor() < 350) and (paddle_r.ycor() + 50 > ball.ycor() > paddle_r.ycor() - 50):
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_l.ycor() + 50 > ball.ycor() > paddle_l.ycor() - 50):
        ball.dx *= -1





