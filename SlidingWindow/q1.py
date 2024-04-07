# s="caberqiitefg"
# s="klkhjgfyyp"
s="aeiouia"
k=3

def countvowel(str):
    c=0
    l={'a','e','i','o','u'}
    for i in range(len(str)):
        if str[i] in l:
            c+=1
    return c

i=0
j=k

map={}
while j < len(s):
    t=s[i:j]
    map[t]=countvowel(t)
    print(map)
    i+=1
    j+=1



max_value = max(map, key=map.get)
if(0!=max_value):
    print(max_value)
else:
    print("Mot Found!")