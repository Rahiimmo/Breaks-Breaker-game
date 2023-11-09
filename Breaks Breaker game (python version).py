import turtle
import random
import math
import winsound


wn = turtle.Screen()
wn.setup(900, 700)
wn.title("Brick Breaker!")
ball = turtle.Turtle()
arrow = turtle.Turtle()
ball.hideturtle()
arrow.hideturtle()
ball.speed(0)
ball.penup()
arrow.penup()
arrow.setpos(0, -299)
ball.right(90)
ball.forward(300)
ball.left(90)
ball.color("green")
ball.forward(162)
ball.left(90)
ball.pd()
ball.color("black")
ball.forward(450)
ball.left(90)
ball.forward(324)
ball.left(90)
ball.forward(486)
ball.left(90)
ball.color("green")
ball.forward(324)
ball.left(90)
ball.color("black")
ball.forward(36)
ball.penup()
ball.setpos(0, -329)
ball.shape("circle")
ball.color("red")
arrow.color('blue')
ball.shapesize(.5)
ball.showturtle()
Resistanse_kam_kon = turtle.Turtle()
Resistanse_kam_kon.speed(0)
Resistanse_kam_kon.ht()
Resistanse_kam_kon.pu()
Resistanse_kam_kon.shape("square")
Resistanse_kam_kon.shapesize(2.5)
Sefid = turtle.Turtle()
Sefid.speed(0)
Sefid.shape("square")
Sefid.shapesize(2.5)
Sefid.color("white")
Sefid.ht()

list_asli = []  # لیستی از مختصات تصادفی انتخاب شده از جایگاه آجرها
resistanse = []  # لیستی از استحکام آجر ها هست
score = 1  # شماره ی مرحله
ghodrat = score / 2  # قدرت توپ در هر مرحله
colors = ['beige', 'bisque', 'palegoldenrod', 'sandybrown', 'chocolate', 'brown', 'maroon', 'saddlebrown']


def init():  # تابع اولیه ی ما که همان لیست های مختصات و استحکام را در هرمرحله ی رسم آجر ، آپدیت می کند
    a = random.randint(2, 3)
    b = [-135, -81, -27, 27, 81, 135]
    c = random.sample(b, a)
    c.sort()
    list_asli.insert(0, c)
    resistanse.insert(0, [score for i in range(len(c))])

y = 123  # مختصه ی y برای ردیف اول آجر
# ما این مختصه را در هرمرحله آپدیت می کنیم.

# کلاسی است که ما ایجاد کردیم جهت شی ء گرایی در اجرای این پروژه. توضیحات کامل را در گزارش پروژه ذکر خواهیم کرد
class Ajor:
    def __init__(self, ListAsli, resistanse):


        self.L1 = ListAsli
        self.L2 = resistanse

        self.turtle = turtle.Turtle()
        self.score_turtle = turtle.Turtle()
        self.score_turtle.ht()
        self.score_print = turtle.Turtle()
        self.score_print.ht()
        self.bye = turtle.Turtle()
        self.bye.ht()
        self.score_turtle.color("blue")
        self.score_turtle.pu()
        self.score_turtle.setpos(170, 125)
        self.score_turtle.pensize(20)
        self.score_turtle.write("Your Score is : " + str(score))

    def besaz(self):

        self.turtle.speed(0)
        self.turtle.ht()
        self.turtle.pu()
        self.turtle.shape("square")
        self.turtle.shapesize(2.5)

        Radif_till_Now = -1  # این متغیر، تعداد ردیف هایی که آجرها تا کنون پایین آمده اند را می شمارد. و درصورت حذف آجر پایین، آپدیت می شود.الگوریتم سر راستی هم دارد
        f = -1
        while f >= ((len(self.L1)) * -1):
            if len(self.L1[f]) != 0:
                break
            else:
                Radif_till_Now = Radif_till_Now - 1
            f = f - 1

        Radif_till_Now = Radif_till_Now + len(self.L1) + 1

        i = 0
        color = None
        indx = None
        while i < len(self.L1):

            if Radif_till_Now >= 9:
                ball.ht()
                ball.clear()
                self.turtle.clear()
                self.score_turtle.clear()
                self.score_print.pu()
                self.score_print.setpos(-50, 50)
                self.bye.pu()
                self.bye.setpos(-50, 0)
                self.score_print.pencolor("blue")
                self.bye.pencolor("green")
                self.score_print.write("Your final score is : " + str(score - 1))
                self.bye.write("Please click on the screen to close the window.")
                wn.exitonclick()

                break

            if i > 0:
                a = self.L1[i]
                b = self.L2[i]

                k = 0
                while k < len(a):
                    if b[k] >= 7:
                        color = colors[7]
                    else:
                        indx = math.ceil(b[k])
                        color = colors[indx - 1]

                    self.turtle.color(color)
                    self.turtle.pencolor("black")
                    self.turtle.setpos(a[k], y - 54 * i)
                    self.turtle.stamp()
                    self.turtle.write(str(b[k]))

                    k += 1


            else:
                a = self.L1[i]
                b = self.L2[i]

                k = 0
                while k < len(a):

                    if b[k] >= 7:
                        color = colors[7]
                    else:
                        indx = math.ceil(b[k])
                        color = colors[indx - 1]

                    self.turtle.color(color)
                    self.turtle.pencolor("black")
                    self.turtle.setpos(a[k], y)
                    self.turtle.stamp()
                    self.turtle.write(str(b[k]))

                    k += 1
            i = i + 1

    def baadi(self):

        self.turtle.speed(0)
        self.turtle.clear()

        Resistanse_kam_kon.clear()
        Resistanse_kam_kon.pu()
        Resistanse_kam_kon.shape("square")
        Resistanse_kam_kon.shapesize(2.5)
        self.score_turtle.clear()
        self.score_turtle.color("blue")
        self.score_turtle.pu()
        self.score_turtle.setpos(170, 125)
        self.score_turtle.pensize(20)
        self.score_turtle.write("Your Score is : " + str(score + 1))




def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def barkhord(i, j):

    global colors
    global list_asli
    global resistanse
    global ghodrat
    winsound.MessageBeep()

    resistanse[i][j] = resistanse[i][j] - ghodrat
    resistanse[i][j] = formatNumber(resistanse[i][j])

    y = 123
    y = y - 54 * i
    x = list_asli[i][j]

    #print (resistanse[i][j])
    if resistanse[i][j] <= 0:
        del resistanse[i][j]
        del list_asli[i][j]
        Sefid.pu()
        Sefid.setpos(x,y)
        Sefid.stamp()
    else:

        if type(resistanse[i][j]) == float:
            color = math.ceil(resistanse[i][j]) -1
        else:
            color = resistanse[i][j] -1

        Resistanse_kam_kon.setpos(x,y)
        Resistanse_kam_kon.color(colors[color])
        Resistanse_kam_kon.pencolor("black")
        Resistanse_kam_kon.stamp()
        Resistanse_kam_kon.write(resistanse[i][j])



def Touch():
    global score
    global ghodrat

    ball.setpos(ball.xcor(), -329.00)
    ball.setheading(90)
    arrow.setpos(ball.xcor(), -299)

    c.baadi()
    score = score + 1
    ghodrat = (score / 2)

# ما براي بازتاب يه درصد خطاي کوچيک رو براي تشخيص دهي پايتون در محل توپ درنظر گرفتيم
# +-2 is for Error(ball radius)

def move():
    global c

    while True:

        i = 0
        while i < len(list_asli):
            for j in list_asli[i]:
                y = (123 - 54 * i)
                x = list_asli[i].index(j)
                y_up = y + 25
                y_down = y - 25
                o = i
                p = x
                a = ball.heading()

                # چهار شرط گوشه آجر
                if j + 25 - 2 < ball.xcor() < j + 25 + 2 and y_down - 2 < ball.ycor() < y_down + 2:
                    if a == 135 or a == 90 or a == 180:
                        ball.right(180)
                        barkhord(o, p)

                    elif 0 < a < 90:
                        ball.right(2 * a)
                        barkhord(o, p)

                    elif 90 < a < 180:
                        ball.right(2 * (a - 90))
                        barkhord(o, p)

                    elif 180 < a < 270:
                        ball.right(2 * a - 180)
                        barkhord(o, p)

                elif j - 25 - 2 < ball.xcor() < j - 25 + 2 and y_down - 2 < ball.ycor() < y_down + 2:
                    if a == 360 or a == 90 or a == 0 or a == 45:
                        ball.right(180)
                        barkhord(o, p)

                    elif 0 < a < 90:
                        ball.right(2 * a)
                        barkhord(o, p)

                    elif 90 < a < 180:
                        ball.left(2 * (180 - a))
                        barkhord(o, p)

                    elif 270 < a < 360:
                        ball.right(2 * (a - 270))
                        barkhord(o, p)

                elif j - 25 - 2 < ball.xcor() < j - 25 + 2 and y_up - 2 < ball.ycor() < y_up + 2:
                    if a == 0 or a == 360 or a == 270 or a == 315:
                        ball.right(180)
                        barkhord(o, p)

                    elif 0 < a < 90:
                        ball.left(2 * (90 - a))
                        barkhord(o, p)

                    elif 180 < a < 270:
                        ball.right(2 * (a - 180))
                        barkhord(o, p)

                    elif 270 < a < 360:
                        ball.left(4 * (a - 270))
                        barkhord(o, p)

                elif j + 25 - 2 < ball.xcor() < j + 25 + 2 and y_up - 2 < ball.ycor() < y_up + 2:
                    if a == 180 or a == 270 or a == 225:
                        ball.right(180)
                        barkhord(o, p)

                    elif 90 < a < 180:
                        ball.right(2 * (a - 90))
                        barkhord(o, p)

                    elif 180 < a < 270:
                        ball.right(2 * (a - 180))
                        barkhord(o, p)

                    elif 270 < a < 360:
                        ball.left(2 * (360 - a))
                        barkhord(o, p)


                # قسمت هاي غير گوشه اي آجر يعني دو ديوار افقي و عمودي

                elif (j - 25 + 2 <= ball.xcor() <= j + 25 - 2) and (
                        y_down - 2 <= ball.ycor() <= y_down + 2 or y_up - 2 <= ball.ycor() <= y_up + 2):

                    ball.right(2 * a)
                    barkhord(o, p)

                elif (y_down + 2 <= ball.ycor() <= y_up - 2) and (
                        j - 25 - 2 <= ball.xcor() <= j - 25 + 2 or j + 25 - 2 <= ball.xcor() <= j + 25 + 2):

                    ball.right(2 * (90 + a))
                    barkhord(o, p)

            i = i + 1

        if ball.ycor() >= 145 or ball.ycor() <= -331:
            if ball.ycor() < -331:
                Touch()
                init()
                c.besaz()

                break

            if ball.xcor() >= 157:
                if ball.heading() >= 43:
                    ball.right(180)

            elif ball.xcor() <= -157:
                if ball.heading() <= 133:
                    ball.right(180)

            else:
                a = ball.heading()
                ball.right(2 * a)

        elif ball.xcor() >= 156 or ball.xcor() <= -156:
            a = ball.heading()
            ball.right(2 * (90 + a))

        ball.forward(2.5)

# onlick function; is used to move mouse cursor.

def onClick(x, y):
    ball.onclick(None)
    a = ball.towards(x, y)
    arrow.setpos(x + 20, y + 20)
    arrow.setheading(a)
    arrow.st()
    ball.onclick(onClick)

def onDrag(x, y):
    ball.ondrag(None)
    a = ball.towards(x, y)
    arrow.setpos(x, y)
    arrow.setheading(a)
    ball.ondrag(onDrag)


def onRelease(x, y):
    ball.onrelease(None)
    arrow.ht()
    a = ball.towards(x, y)
    ball.setheading(a)
    ball.onrelease(onRelease)
    move()


def onkey_clockwise():
    arrow.st()
    arrow.right(20)
    wn.onkey(onkey_clockwise, "Right")


def onkey_counterclockwise():
    arrow.st()
    arrow.left(20)
    wn.onkey(onkey_counterclockwise, "Left")


def onkey_forward():
    arrow.st()
    arrow.forward(5)
    wn.onkey(onkey_forward, "Up")


def onkey_backward():
    arrow.st()
    arrow.backward(5)
    wn.onkey(onkey_backward, "Down")


def onkey_release():
    a = ball.towards(arrow.xcor(), arrow.ycor())
    ball.setheading(a)
    arrow.ht()
    move()


wn.listen()
wn.onkey(onkey_release, "F")
wn.onkey(onkey_clockwise, "Right")
wn.onkey(onkey_counterclockwise, "Left")
wn.onkey(onkey_forward, "Up")
wn.onkey(onkey_backward, "Down")

# our main function; that is an infinity loop for the ball ,of course with some limitations

def main():
    ball.onclick(onClick)
    ball.ondrag(onDrag)
    ball.onrelease(onRelease)

init()
khali = []
c = Ajor(list_asli, resistanse)
c.besaz()

main()
wn.mainloop()
