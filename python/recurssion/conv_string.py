import time

start_time = time.perf_counter()

def conv_str(n, base, s):
    if base == 10:
        if n != 0:
            x = n % base
            return(conv_str(n // base, base, str(x) + s))
        else:
            return s
    elif base == 16:
        convertString = "0123456789ABCDEF"
        if n != 0:
            return (conv_str(n // base, base, convertString[n % base] + s))
        else:
            return s


print(conv_str(1453, 16, ""))

print(time.perf_counter() - start_time)