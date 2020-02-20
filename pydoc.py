import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.delay(0)
s.tracer(0, 0)
s.setworldcoordinates(-1, -1, 1, 1)
t.ht()

x1 = -6
y1 = 0
x2 = 6
y2 = 0
xb = 0
yb = 0
xspeed = 0.005
yspeed = 0 #0.005

def player1():
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.begin_fill()
    t.goto(x1, y1+1)
    t.goto(x1+0.5, y1+1)
    t.goto(x1+0.5, y1-1)
    t.goto(x1, y1-1)
    t.goto(x1, y1+1)
    t.end_fill()
    t.pu()
    
def player2():
    t.pu()
    t.goto(x2, y2)
    t.pd()
    t.begin_fill()
    t.goto(x2, y2-1)
    t.goto(x2-0.5, y2-1)
    t.goto(x2-0.5, y2+1)
    t.goto(x2, y2+1)
    t.goto(x2, y2-1)
    t.end_fill()
    t.pu()
    
def ball():
    t.pu()
    t.goto(xb, yb)
    t.pd()
    t.begin_fill()
    t.goto(xb-0.5, yb+0.5)
    t.goto(xb+0.5, yb+0.5)
    t.goto(xb+0.5, yb-0.5)
    t.goto(xb-0.5, yb-0.5)
    t.goto(xb-0.5, yb+0.5)
    t.end_fill()
    t.pu()
    
def player1_up():
    global y1
    y1 += 1
def player1_down():
    global y1
    y1 -= 1
    
def player2_up():
    global y2
    y2 += 1
def player2_down():
    global y2
    y2 -= 1
    
s.onkey(player1_up, "w")
s.onkey(player1_down, "s")
s.onkey(player2_up, "Up")
s.onkey(player2_down, "Down")

s.listen()

while True:
    if y1 < -5:
        y1 += 1
    if y1 > 5:
        y1 -= 1
    
    if y2 < -5:
        y2 += 1
    if y2 > 5:
        y2 -= 1
    t.clear()
    player1()
    player2()
    ball()
    
    if yb < -5.5 or yb > 5.5:
        yspeed *= -1
        
    if xb < -5.5 or xb > 5.5:
        xspeed *= -1
    xb += xspeed
    yb += yspeed
    s.delay(0)
    s.tracer(0, 0)
    s.setworldcoordinates(-6, -6, 6, 6)
    s.update()
