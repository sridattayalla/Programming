n = int(input())
str_num = ""
nums = [int(x) for x in input().split(" ")]

exchanges = []
for i in range(n):
    exc = input()
    for j in range(n):
        if(exc[j] == 'Y'):
            exchanges.append([i, j])


def change(list, nms):
    if(len(list) == 0):
        return nms
    else:
        for i in range(len(list)):
            temp_str = nms[:]
            temp_str[list[i][0]], temp_str[list[i][1]] = temp_str[list[i][1]], temp_str[list[i][0]]
            lex_small = True
            for j in range(len(temp_str)):
                if(temp_str[j] > nms[j]):
                    lex_small = False
                    break
                if(temp_str[j] < nms[j]):
                    lex_small = True
                    break
            if lex_small:
                return change(list[0:i]+list[i+1:], temp_str)
            else:
                return change(list[:], nms)
new_nums = change(exchanges, nums)
print(" ".join([str(x) for x in new_nums]))