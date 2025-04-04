f=[int(i) for i in open('17 (3).txt').read().split()]
ma = max([i for i in f if abs(i)%100 == 36])
d=[]
for i in range(len(f)-2):
    s = [j for j in f[i:i+3] if j>0 and abs(j)%100==36]
    if len(s)>=2 or sum(f[i:i+3]) <= ma:
        d.append(sum(f[i:i+3]))
print(len(d), min(d))