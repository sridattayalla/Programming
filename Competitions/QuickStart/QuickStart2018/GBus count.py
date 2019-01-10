t = int(input())
for i in range(t):
    bus_cout = int(input())
    temp_str = input()
    if(temp_str[len(temp_str)==" "]):
        temp_str =temp_str[:-1]
    temp = [int(x) for x in temp_str.split(" ")]
    cities_travel = []
    for j in range(bus_cout):
        cities_travel.append([temp[j*2], temp[j*2+1]])

    cities_count = int(input())
    output_list =[]
    for j in range(cities_count):
        count = 0
        city = int(input())
        for k in cities_travel:
            if(k[0]<=city and city<=k[1]):
                count += 1
        output_list.append(count)

    print("Case #"+str(i+1)+": "+" ".join([str(x) for x in output_list]))
    if(i!=t-1):
        blank = input()