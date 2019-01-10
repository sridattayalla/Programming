
exp_op = int(input())
N = int(input())

def fun(total, i):
    if total == 0:
        return 1
    s = 0
    j = i
    while not (j ** N) > total :
        s += fun(total - j ** N, j+1)
        j +=1
    return s

print(fun(exp_op, 1))