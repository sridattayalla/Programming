str_n, str_m = input().split()
n = int(str_n)
m = int(str_m)
constitutions = []
for _ in range(n):
    constitutions.append(list(int(x) for x in input().split()))
horse_tradings = []
ht_count = int(input())
for _ in range(ht_count):
    horse_tradings.append(list(int(x) for x in input().split()))

B = 2
if(n == m and n!=2):
    B = n//2
elif(n == 2 or m == 2):
    B = 1

def wins(n, m, B, before):
    AAA = 0
    BBB = 0
    othres = 0
    for i in range(n // B):
        for j in range(m // B):
            a = 0
            b = 0
            o = 0
            for k in range(B):
                for l in range(B):
                    seat = constitutions[k + i * B][l + j * B]
                    if (seat == 1):
                        a += 1
                    elif (seat == 2):
                        b += 1
                    else:
                        o += 1
            if ((b >= o and a > b) or (o > b and a > o)):
                AAA += 1
            elif ((b > a and a >= o) or (o > a and b > a) ):
                BBB += 1
            elif(((o>a) and (a>=b)) or ((o>b) and (b>=a))):
                othres += 1

    if (AAA > BBB and BBB >= othres) or (othres > BBB and AAA > othres):
        if before:
            print("Initial Majority Party:Seats = AAA:" + str(AAA))
        else:
            print("Party Won Party:Seats = AAA:" + str(AAA))
    elif (BBB > AAA and AAA >= othres) or (BBB > othres and othres >= AAA):
        if before:
            print("Initial Majority Party:Seats = BBB:" + str(BBB))
        else:
            print("Party Won Party:Seats = BBB:" + str(BBB))

    elif (othres > AAA and AAA >= BBB) or (othres > BBB and BBB >= AAA):
        if before:
            print("Initial Majority Party:Seats = Others:" + str(othres))
        else:
            print("Party Won Party:Seats = Others:" + str(othres))
    else:
        if before:
            print("No Majority")
        else:
            print("No Majority")

wins(n, m, B, True)

# after horse trading
for i in range(ht_count):
    constitutions[horse_tradings[i][0]-1][horse_tradings[i][1]-1] = horse_tradings[i][2]
wins(n, m, B, False)