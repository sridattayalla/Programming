
list = []

def check(password):
    if len(password) == 0:
        return []
    for i in range(1, len(password) + 1):
        if password[0: i] in list:
            res = [password[0 : i]]
            return res + check(password[i : len(password)])
            break
        elif i == len(password):
            return ["WRONG PASSWORD"]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list = input().strip().split(' ')
    attempt = input().strip()
    temp = check(attempt)
    if "WRONG PASSWORD" in temp:
        print("WRONG PASSWORD")
    else:
        print(" ".join(temp))