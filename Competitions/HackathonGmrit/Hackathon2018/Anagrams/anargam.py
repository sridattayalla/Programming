import string

f = open("sample1.txt", "r")
anargam_txt = f.read()

#removing special characters in str
anargam_txt = anargam_txt.replace("\n", " ")
str = "".join([x for x in anargam_txt if x in string.ascii_letters + " " ])
words = [x for x in str.split(" ") if len(x)>= 4]

out_put = []

#fun to check possibility
def is_possible(temp, ref):
    if(len(temp) == len(ref) and temp.lower() != ref.lower()):
        for i in range(len(temp)):
            if(temp[i].lower() not in ref.lower()):
                return False
        return True
    else:
        return False

while len(words) > 0:
    temp = words[0]
    anargams = [temp]
    del words[0]
    pos = 1
    while pos < len(words):
        if(is_possible(temp, words[pos])):
            if words[pos] not in anargams:
                anargams.append(words[pos])
            del words[pos]
        else:
            pos += 1
    if(len(anargams) > 1):
        anargams.sort()
        out_put.append(",".join(anargams))


out_put.sort()
for i in range(len(out_put)):
    print(out_put[i])