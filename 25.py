from fnmatch import *
s=0
i = 1799999999
while i >10**6:
    if fnmatch(str(i), '17*023?9') and sum((map(int, list(str(i)))))%11==0 and i<10**10:
        print(i, sum((map(int, list(str(i)))))/11, sum((map(int, list(str(i))))))
        s+=1
    if str(i)[:2] =='17':
        i-=1
    else:
        i-=1000000
    if s==6:
        break