# s="caberqiitefg"
s="klkhjgfyyp"
k=5
i=0
j=k

def countvowel(str):
    c=0
    l=['a','e','i','o','u']
    for i in range(len(str)):
        if str[i] in l:
            c+=1
    return c

# st=set(l)
# print(st)
map={}
while j < len(s):
    t=s[i:j]
    map[t]=countvowel(t)
    print(map)
    i+=1
