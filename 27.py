from turtle import *
from math import dist
from random import *
def fun(n):
    m=10**10
    for i in n:
        s=0
        x1, y1 = i
        for j in n:

            s+=dist(i, j)
        if s<m:
            m=s
            xn=x1
            yn = y1
        return xn, yn
f = open('27_A.txt').read().split('\n')
data = []
for i in f:
    data.append(list(map(float, i.split())))
# print(data)
tracer(0)
screensize(2000, 2000)
clastert =[]
while data:
    cl=[data.pop()]
    for p in cl:
        sosed =[p1 for p1 in data if dist(p,p1)<5]
        cl.extend(sosed)
        for p1 in sosed:
            data.remove(p1)
    clastert.append(cl)

xa = sum(fun(x)[0] for x in clastert)
ya = sum(fun(y)[1] for y in clastert)
print(xa, ya)
up()
for j in clastert:
    col = (random(),random(),random())
    for x, y in j:
        goto(x*2,y*2)
        dot(3, col)
    update()
done()