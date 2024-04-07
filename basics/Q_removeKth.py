def removeKth(s,k):
    if (k<0 or k>(len(s)-1) ):
        return s
    else:
        sn=''
        for i in range(len(s)):
            if k==i:
                continue
            else:
                sn+=s[i]
        return sn
    
s=input("enter a string : ")
k=int(input("enter va index number ;"))
print(removeKth(s,k))