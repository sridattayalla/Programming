t = int(input())
for i in range(1,t+1):
    inp = [x for x in input().split(" ")]
    R = int(inp[0])
    C = int(inp[1])
    H = int(inp[2])
    V = int(inp[3])
    waffle = []
    for _ in range(R):
        wallfle_line = input()
        temp_waffle_line = []
        for waffle_pos in range(C):
            temp_waffle_line.append(wallfle_line[waffle_pos])
        waffle.append(temp_waffle_line)

