from math import *
for i in range(1, 10000):
    s = ceil((ceil(log2(16+52))*i)/8)
    if s*3000<=1450*2**10:
        print(i)