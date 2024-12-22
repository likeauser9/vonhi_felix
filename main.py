import turtle

pen = turtle.Turtle()
window = turtle.Screen()
window.title("Вонхи + Феликс = ❤")
window.bgcolor("black")

pen.speed(1)
pen.width(3)
pen.color("white")

def draw_V():
  pen.penup()
  pen.goto(-450, 350)
  pen.pendown()
  pen.goto(-450, 250)
  pen.goto(-400, 275)
  pen.goto(-450, 300)
  pen.goto(-400, 325)
  pen.goto(-450, 350)

def draw_O():
  pen.penup()
  pen.goto(-350, 340)
  pen.pendown()
  pen.goto(-350, 260)
  pen.goto(-340, 250)
  pen.goto(-310, 250)
  pen.goto(-300, 260)
  pen.goto(-300, 340)
  pen.goto(-310, 350)
  pen.goto(-340, 350)
  pen.goto(-350, 340)

def draw_N():
  pen.penup()
  pen.goto(-250, 350)
  pen.pendown()
  pen.goto(-250, 250)
  pen.goto(-250, 300)
  pen.goto(-200, 300)
  pen.goto(-200, 350)
  pen.goto(-200, 250)

def draw_H():
  pen.penup()
  pen.goto(-150, 350)
  pen.pendown()
  pen.goto(-100, 250)
  pen.penup()
  pen.goto(-100, 350)
  pen.pendown()
  pen.goto(-150, 250)

def draw_I():
  pen.penup()
  pen.goto(-50, 350)
  pen.pendown()
  pen.goto(-50, 250)
  pen.goto(0, 350)
  pen.goto(0, 250)

def draw_plus():
  pen.penup()
  pen.goto(75, 300)
  pen.pendown()
  pen.goto(75, 250)
  pen.penup()
  pen.goto(50, 275)
  pen.pendown()
  pen.goto(100, 275)

def draw_F():
  pen.penup()
  pen.goto(-425, 200)
  pen.pendown()
  pen.goto(-440, 200)
  pen.goto(-450, 190)
  pen.goto(-450, 160)
  pen.goto(-440, 150)
  pen.goto(-410, 150)
  pen.goto(-400, 160)
  pen.goto(-400, 190)
  pen.goto(-410, 200)
  pen.goto(-425, 200)
  pen.goto(-425, 100)

def draw_E():
  pen.penup()
  pen.goto(-350, 200)
  pen.pendown()
  pen.goto(-350, 100)
  pen.goto(-300, 100)
  pen.penup()
  pen.goto(-350, 150)
  pen.pendown()
  pen.goto(-300, 150)
  pen.penup()
  pen.goto(-350, 200)
  pen.pendown()
  pen.goto(-300, 200)

def draw_L():
  pen.penup()
  pen.goto(-250, 100)
  pen.pendown()
  pen.goto(-225, 200)
  pen.goto(-200, 100)

def draw_I2():
  pen.penup()
  pen.goto(-150, 200)
  pen.pendown()
  pen.goto(-150, 100)
  pen.goto(-100, 200)
  pen.goto(-100, 100)

def draw_K():
  pen.penup()
  pen.goto(-50, 200)
  pen.pendown()
  pen.goto(-50, 100)
  pen.goto(-50, 150)
  pen.goto(0, 200)
  pen.goto(-50, 150)
  pen.goto(0, 100)

def draw_S():
  pen.penup()
  pen.goto(100, 190)
  pen.pendown()
  pen.goto(90, 200)
  pen.goto(60, 200)
  pen.goto(50, 190)
  pen.goto(50, 110)
  pen.goto(60, 100)
  pen.goto(90, 100)
  pen.goto(100, 110)

def draw_equal():
  pen.penup()
  pen.goto(150, 150)
  pen.pendown()
  pen.goto(200, 150)
  pen.penup()
  pen.goto(150, 100)
  pen.pendown()
  pen.goto(200, 100)

# def draw_heart():
#   for i in range(200):
#     pen.right(1)
#     pen.forward(1)

def draw_heart():
  pen.penup()
  pen.goto(0, -150)
  pen.pensize(3)
  pen.pendown()
  pen.color("red")
  pen.begin_fill()
  pen.left(50),
  pen.forward(133)
  pen.circle(50, 200)
  pen.right(140)
  pen.circle(50, 200)
  pen.forward(133)
  pen.end_fill()

draw_V()
draw_O()
draw_N()
draw_H()
draw_I()
draw_plus()
draw_F()
draw_E()
draw_L()
draw_I2()
draw_K()
draw_S()
draw_equal()
# pen.penup()
# pen.goto(0, -200)
# pen.pendown()
# pen.color('pink', 'red')
# pen.begin_fill()
# pen.left(140)
# pen.forward(111.65)
# draw_heart()
# pen.left(120)
# draw_heart()
# pen.forward(111.65)
# pen.end_fill()
draw_heart()

pen.hideturtle()

window.mainloop()