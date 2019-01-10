import string, math
text = input()

is_negative = False
if(text[0] == "-"):
    is_negative = True

nums = "".join([x for x in text if x in string.digits])
if not is_negative:
    if len(nums) == 3:
        print(-1)
    else:
        num_list = [int(x) for x in nums[0:math.floor(len(nums)/2)]]
        pos = math.floor(len(nums)/2) -1
        while True:
            if(pos == 0):
                print(-1)
                break
            elif(num_list[pos] > num_list[pos - 1]):
                num_list[pos], num_list[pos -1] = num_list[pos-1], num_list[pos]
                if(len(nums) % 2 == 1):
                   print("".join([str(x) for x in num_list]) + str(nums[len(num_list)]) + "".join([str(x) for x in reversed(num_list)]))
                else:
                    print("".join([str(x) for x in num_list]) + "".join([str(x) for x in reversed(num_list)]))

                break
            else:
                pos -= 1

else:
    if len(nums) == 3:
        print(-1)
    else:
        num_list = [int(x) for x in nums[0:math.floor(len(nums) / 2)]]
        pos = math.floor(len(nums) / 2) - 1
        while True:
            if (pos == 0):
                print(-1)
                break
            elif (num_list[pos] < num_list[pos - 1]):
                num_list[pos], num_list[pos - 1] = num_list[pos - 1], num_list[pos]
                if (len(nums) % 2 == 1):
                    print( "-" + "".join([str(x) for x in num_list]) + str(nums[len(num_list)]) + "".join(
                        [str(x) for x in reversed(num_list)]))
                else:
                    print("-" + "".join([str(x) for x in num_list]) + "".join([str(x) for x in reversed(num_list)]))

                break
            else:
                pos -= 1