#input
list = [int(x) for x in input().split(" ")]


#recursive fun
#base cases :
#if n => len(list): return true
#if list[n] == 0: return false
def possibility(n) :
    if n >= len(list) :
        return True
    elif list[n] == 0 :
        return False
    else:
        for i in range(1, list[n] + 1) :
            result = possibility(n + i)
            if result :
                return True
    return False

#logic:
#possiblity(4) == posiblity(list[n+1]) or possibility(list[n+2]) or ... or possibility(list[n+3])

# calling
print(possibility(0))