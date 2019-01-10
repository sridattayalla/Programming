list = [int(x) for x in input().split(" ")]
number_to_search = int(input("Enter a number to search: "))

for i in range(len(list)):
    if number_to_search == list[i] :
        print("Index of ", number_to_search, " is ", i)
        break
    elif (i == len(list) - 1):
        print("No such an entry in list!")