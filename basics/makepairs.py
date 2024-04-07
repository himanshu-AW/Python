def makepairs(l1,l2):
    l=[]
    if len(l1) and len(l2):
            if len(l1)<len(l2):
                l=[ (l1[i],l2[i]) for i in range(len(l1))]
            else :
                l=[ (l1[i],l2[i]) for i in range(len(l2))]

            # for i in range(len(l1)):
            #       t=(l1[i],l2[i])
            #       l.append(t)
            #  second method
            return l
a=[1,3,5,7,8,10,23,3]
b=[2,4,6,8,10,23,3]
res=makepairs(a,b)
print(res)