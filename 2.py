from itertools import *
def f(x,y,z,w):
    return (z<=x)and((not y)and((not w)==y))

for a in product([0,1],repeat=5):
    row  = [(0,1,a[0], 0), (1,a[1], 0, a[2]),(0,1,1,a[3]),(a[4], 1,1,1)]
    val = [0,0,1,1]
    if len(set(row))==len(row):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, p))) for p in row]==val:
                print(i)
