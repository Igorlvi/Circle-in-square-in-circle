# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import turtle
import math


print("Розрахуйте S площу квадрата та P периметр.\nРозрахуйте r радіус вписаного та R описаного кола даного квадрата")
print("Накресліть квадрат з вписаним та описаним колом")
print("Введіть розмір сторони у см ?")
a = float(input("a = "))
r = a/1.414
R = a/2
m = a**2+((a/2)**2)
l = math.sqrt(m)
print("Периметр P = %.2f" % ((a+a)*2))
print("Площа = %.2f" % (a * a))
print("R радіус описаного кола = %.2f" % (r))
print("r радіус вписаного кола = %.2f" % (a / 2))
print ("Поки Ви звіряєте свій розв'язок, дана програма побудує Вам Ваш квадрат з вписаним та описаним колом")
print("Щоб підтвердити дію введіть yes (y) та enter")
figure = input("Підтвердити (y) ?  : ")
if figure == 'y':
    turtle.forward(a*37)
    turtle.left(90)
    turtle.forward(a*37)
    turtle.left(90)
    turtle.forward(a*37)
    turtle.left(90)
    turtle.forward(a*37)
    turtle.left(45)
    turtle.circle(r*37)
    turtle.left(45)
    turtle.forward(a*37/2)
    turtle.circle(R*37)
    turtle.left(63)
    turtle.forward(l*37)
    turtle.up()
    turtle.goto(-200+R,-200+R)
    turtle.down()
    turtle.hideturtle()
    style = ('Courier', 20, 'italic')
    turtle.write(" S площа квадрата\n Перелік усіх формул\n S = a²\n S = 2R²\n S = 4r²\n S = P²/16\n S = d²/2\n S = 16L²/√5\n ДЕ\n а-сторона квадрата\n R-радіус описаного кола\n r-радіус вписаного кола\n P-периметр квадрата\n d-діаметр вписаного кола\n L- відрізок зображений на рисунку", font=style, align='right')
    turtle.title("Ваш квадрат з вписаним та описаним колом ")

else:
    print("Помилка введення ???")


