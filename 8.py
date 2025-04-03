from itertools import *
k=0
for i in product('АВЕНС', repeat=5):
    s=''.join(i)
    if s[0] == 'Н' and s.count('В') ==2:
        if s.count('А') <=1 and s.count('Е') <=1 and s.count('Н') <=1 and s.count('С') <=1:
            k+=1
print(k)