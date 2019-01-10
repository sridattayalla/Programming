import math
def is_possible(a, b, perimeter):
    c = math.sqrt(((a**2)+(b**2))-1)
    int_c = int(c)
    if((c-int_c)==0 and a+b+c <= perimeter):
        return True
    else:
        return False
def find_triagles(perimeter):
    count = 0
    for i in range(1, perimeter-1):
        for j in range(i, perimeter-1):
            if(i+j < perimeter and is_possible(i, j, perimeter)):
                count += 1
    print(count)
for _ in range(int(input())):
    find_triagles(int(input()))