
P=[i for i in range(5,1000, 5)]
Q=[i for i in range(3,1000, 3)]
a=[]
d=[]
for x in range(1, 1000):
    if not ((x in Q)<=((x in P)<=(x in Q) and (x in a))):
        d.append(x)
print(d)
print(15)
