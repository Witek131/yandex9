s=[0]*50000
for i in range(20000):
    if i<3:
        s[i] =1
    elif i%2==0:
        s[i] = s[i-1]*(i-1)
    else:
        s[i] = s[i - 2] * (2*i - 2)
print((s[10048]-s[10045])/s[10043])