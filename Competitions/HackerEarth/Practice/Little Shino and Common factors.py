import sys
import math

a, b = map(int, sys.stdin.readline().split())
d = math.gcd(a,b)

if(d!=1):
    count = 0
    x = 1
    add = 1
    if(d%2!=0):
        add = 2
    while(x<math.sqrt(d)):
        if(d%x==0):
            count += 2
        x += add
    if(math.sqrt(d)%1==0):
        count += 1
    print(count)
else:
    print(1)