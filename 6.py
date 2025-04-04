from turtle import *
print(14)
tracer(0)
screensize(2000, 2000)
k=10
for i in range(3):
    fd(5*k)
    rt(90)
    fd(12 * k)
    rt(90)
up()
fd(3 * k)
rt(90)
fd(2 * k)
rt(90)
down()
for i in range(4):
    fd(5 * k)
    rt(90)
    fd(12 * k)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(3, 'red')
update()
done()