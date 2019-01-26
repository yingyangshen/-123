#直接输出个人信息
def my_intrduce(name,sex,birthday):
    print("我的姓名是：",str(name),"\n我的性别是：",str(sex),"\n我的生日是：",str(birthday))
my_intrduce("应洋深","男","1995年12月7日")
#自己导入式
first_name = input("你姓什么？")
last_name = input("你名字是什么？")
full_name = str(first_name)+str(last_name)
birth_year = int(input("你出生于哪一年？"))
how_old = 2019-birth_year
id_card = int(input("请输入身份证倒数第二位数："))
if id_card==1:
    xingbie="男"
else:
    xingbie="女"
print("我的姓名是：",str(full_name),"\n我的性别是：",str(xingbie),"\n我今年",str(how_old),"岁了")

# mesage = "Hello Python Crash Course reader!"
# print(mesage)
#'I told my friend, "Python is my favorite language!"'

#"The language 'Python' is named after Monty Python, not the snake."
#"One of Python's strengths is its diverse and supportive community."

#name = "ada lovelace"
#print(name.title())

    #name = "Ada Lovelace"
    #print(name.upper())
    #print(name.lower())

#first_name = "ada"
#last_name = "lovelace"
#full_name = first_name + " " + last_name
#print(full_name)

#first_name = "ada"
#last_name = "lovelace"
#full_name = first_name + " " + last_name
#print("Hello, " + full_name.title() + "!")

#first_name = "ada"
#last_name = "lovelace"
#full_name = first_name + " " + last_name
#message = "Hello, " + full_name.title() + "!"
# #print(message)

#age = 23
#message = "Happy " + str(age) + "rd Birthday!"
#print(message)

#画鼻子
import turtle as t
def draw_bizi():
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.seth(-30)
    t.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a+0.08
            t.lt(3)
            t.fd(a)
        else:
            a = a-0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    t.pu()
    t.seth(90)
    t.fd(25)
    t.seth(0)
    t.fd(10)
    t.pd()
    t.pencolor(255, 155, 192)
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()
    t.pu
    t.seth(0)
    t.fd(20)
    t.pd()
    t.pencolor(255, 155, 192)
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82,45)
    t.end_fill()

#画身体
import turtle as t


def draw_body():
    """
    画小猪佩奇的身体
    :return: null
    """
    t.color((255, 99, 71), "red")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-78)
    t.pd()
    t.begin_fill()
    t.seth(-130)
    t.circle(100, 10)
    t.circle(300, 30)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300, 30)
    t.circle(100, 3)
    t.color((255, 155, 192), (255, 100, 100))
    t.seth(-135)
    t.circle(-80, 63)
    t.circle(-150, 24)
    t.end_fill()

#画耳朵
import turtle as t


def draw_ear():
    t.color((255, 255, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    t.pu()
    t.seth(90)
    t.fd(-12)
    t.seth(0)
    t.fd(30)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()

#画眼睛
import turtle as t
def draw_eyes():

    t.color((255, 155, 192), "white")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-95)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color((255, 155, 192), "white")
    t.pu()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

#画手
import turtle as t
def draw_hands():
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(-40)
    t.seth(0)
    t.fd(-27)
    t.pd()
    t.seth(-160)
    t.circle(300, 15)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-10)
    t.circle(-20, 90)
    t.pu()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(237)
    t.pd()
    t.seth(-20)
    t.circle(-300, 15)
    t.pu()
    t.seth(90)
    t.fd(20)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-170)
    t.circle(20, 90)

#画头
import turtle as t
def draw_head():
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.begin_fill()
    t.seth(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60,-95)
    t.seth(161)
    t.circle(-300, 15)
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i <90:
            a += 0.08
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()

#画脚
import turtle as t
def draw_legs():
    t.pensize(10)
    t.color((240, 128, 128))
    t.pu()
    t.seth(90)
    t.fd(-75)
    t.seth(0)
    t.fd(-180)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)
    t.pensize(10)
    t.color((240, 128, 128))
    t.pu()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)
#画嘴
import turtle as t
def draw_mouse():
    t.color((239, 69, 19))
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(-100)
    t.pd()
    t.seth(-80)
    t.circle(30, 40)
    t.circle(40, 80)

#画尾巴
import turtle as t
def draw_weiba():

    t.pensize(4)
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(70)
    t.seth(0)
    t.fd(95)
    t.pd()
    t.seth(0)
    t.circle(70, 20)
    t.circle(10, 330)
    t.circle(70, 30)

#画sai
import turtle as t
def draw_sai():
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(-95)
    t.seth(0)
    t.fd(65)
    t.pd()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

