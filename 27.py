from turtle import *
f = open('27_A.txt').read().split('\n')
data = []
for i in f:
    data.append(list(map(float, i.split())))
print(data)
tracer(0)
screensize(2000, 2000)
up()
for x, y in data:
    goto(x*3,y*3)
    dot(3, 'red')
update()
done()