t = int(input())
nums = ([x for x in input().split(" ")])

initNum = "".join(nums)
temp = nums[:]
temp.sort()
endNum = "".join(temp)

g = {}

def addTograph(key):
    for i in range(2,t+1):
        temp_item = key[0:i]
        rev = temp_item[::-1]
        if(i==2):
            new_item = (rev + key[i:])
            g[key] = [new_item]
        if(i==t):
            new_item = rev
            g[key].append(new_item)
        else:
            new_item = (rev + key[i:])
            g[key].append(new_item)

visited = []
q = [initNum]
lengths = {initNum:0}
if(t>1 and initNum!=endNum):
    while(len(q)>0):
        currNum = q.pop(0)
        addTograph(currNum)
        for each in g[currNum]:
            if(each not in visited):
                visited.append(each)
                lengths[each] = lengths[currNum] + 1
                if(each == endNum):
                    q = []
                    print(lengths[endNum])
                    break
                else:
                    q.append(each)
else:
    print(lengths[endNum])