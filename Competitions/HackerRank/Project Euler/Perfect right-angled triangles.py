import math
for _ in range(int(input())):
    count = 0
    rt = 0
    _C = int(input())
    visited = [False]*_C
    for c in range(5,_C):
        for a in range(c):
            if not visited[a]:
                b = math.sqrt((c**2)-(a**2))
                sqrt_c = math.sqrt(c)
                if((b- int(b)) == 0):
                    rt += 1
                    if((sqrt_c-int(sqrt_c))==0 and math.gcd(a,int(b))==1 and math.gcd(int(b), int(c))==1):
                        s = (a+b+c)/2
                        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
                        if(area%6 ==0 and area%28==0):
                            count += 1
                    visited[int(b)] = True
            visited[a] = True

    print(count)