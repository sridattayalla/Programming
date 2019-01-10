from stack import stack

s = stack()

def conv_str(n, base):
    if base == 10:
        if n > 0:
            s.push(n % base)
            conv_str(n//base, base)
    elif base == 16:
        convertString = "0123456789ABCDEF"
        if n > 0:
            s.push(convertString[n % base])
            conv_str(n // base, base)
    else:
        print("enter 10 or 16")


conv_str(1453,10)

s.reverse()

print("".join(str(x) for x in s.stack))




