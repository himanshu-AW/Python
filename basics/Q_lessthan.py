# lessthan
def lessthan(lst,k):
    # ln=list()
    # for i in lst:
    #     if i<k:
    #         ln.append(i)
    # return ln
    ln=[x for x in lst if x < k ]
    return ln

lst=input("Enter a list numbers : ").split()
print(lst)
lst=[int(x) for x in lst]
k=input("Enter a key number : ")
nlst=lessthan(lst,int(k))
print(nlst,' lessthan the  ',int(k),'key number')
