# Sample bash code
t = int(input())

def are_inline(x1, y1, x2, y2, x3, y3):
    if((y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)):
        return True
    else:
        return False

for i in range(t):
    str_xa, str_ya = input().split(" ")
    str_xb, str_yb = input().split(" ")
    str_xc, str_yc = input().split(" ")
    str_xd, str_yd = input().split(" ")
    xa = int(str_xa)
    ya = int(str_ya)
    xb = int(str_xb)
    yb = int(str_yb)
    xc = int(str_xc)
    yc = int(str_yc)
    xd = int(str_xd)
    yd = int(str_yd)
    if(are_inline(xa, ya, xb, yb, xc, yc)):
        print("Yes")
    elif(are_inline(xa, ya, xd, yd, xc, yc)):
         print("Yes")
    elif(are_inline(xb, yb, xd, yd, xc, yc)):
         print("Yes")
    elif(are_inline(xa, ya, xd, yd, xb, yb)):
         print("Yes")
    else:
        print("No")




