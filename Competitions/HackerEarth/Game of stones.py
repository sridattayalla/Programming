str_n , str_q = input().split(" ")
N = int(str_n)
Q = int(str_q)

str_input = input()
nums= []
for i in range(2*N-1):
    if(i % 2 == 0):
        nums.append(int(str_input[i]))

for i in range(Q):
    count = 0
    l = [int(x) for x in input().split(" ")]
    start = l[0]
    end = l[1]
    for j in range(start-1 , end):
        count += nums[j]//2 + 1
    if(count%2==0):
        print("Hacker")
    else:
        print("Mishki")


