f = open('9.csv').read().split('\n')
k = 0
for i in f:
    s=[int(j) for j in i.split(',')]
    s2 = [x for x in s if s.count(x) >= 2]
    s1 = [x for x in s if s.count(x) == 1]
    if len(set(s2)) == 2 and sum(s2) < sum(s1):
        k+=1
print(k)