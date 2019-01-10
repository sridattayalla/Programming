t = input()
list = [int(x) for x in input().split(" ")]

missing_nums = []
excess_nums = {}
has_chance = {}

# finding missing and excess numbers
for i in range(1, len(list)+1, 1):
    if(i not in list):
        missing_nums.append(i)
    else:
        l = []
        for j in range(len(list)):
            if (i == list[j]):
                l.append(j)
        if (len(l) > 1):
            has_chance[i] = True
            excess_nums[i] = l



# replacing nums
for i in range(len(list)):
    if((list[i] in excess_nums.keys())):
        if(missing_nums[0] > list[i]):
            if(has_chance[list[i]]):
                has_chance[list[i]] = False
                del excess_nums[list[i]][0]
            else:
                if (len(excess_nums[list[i]]) > 1 or (len(excess_nums[list[i]]) == 1 and not has_chance[list[i]])):
                    del excess_nums[list[i]][0]
                    list[i] = missing_nums[0]
                    del missing_nums[0]

        else:
            if (len(excess_nums[list[i]]) > 1 or (len(excess_nums[list[i]]) == 1 and not has_chance[list[i]])):
                del excess_nums[list[i]][0]
                list[i] = missing_nums[0]
                del missing_nums[0]


print(list)






