list = [int(x) for x in input().split(" ")]

# loop the list to check if suceeding number is less than preceeding number
# if it is less, then make a reverse inner loop to fit that number
for i in range(len(list) - 1) :
    if( list[i] > list[i + 1]):
        if i == 0:
            list.insert(0, list[i + 1])
            del list[i + 2]
        else:
            for j in range(i - 1, -1, -1):
                if j == 0:
                    list.insert(j, list[i + 1])
                    del list[i + 2]
                    print(list)
                    break
                elif(list[i + 1] >= list[j]):
                    list.insert(j + 1, list[i + 1])
                    del list[i + 2]
                    print(list)
                    break




