t = int(input())
for _ in range(t):
    p = int(input())
    dict = {}
    input_str = input()
    list = []
    for i in range(2*p - 1):
        if(i % 2 == 0):
            list.append(int(input_str[i]))
    for i in list:
        if (i in dict):
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    max_num = 0
    sorted(dict, reverse=True)
    outs = {}
    for i in dict:
        if(dict[i]  in outs):
            outs[dict[i]] = outs[dict[i]]+[i]
        else:
            outs[dict[i]] = [i]
    sorted(outs, reverse=True)
    max_key = max(outs, key=int)
    print(" ".join(str(x) for x in outs[max_key]))