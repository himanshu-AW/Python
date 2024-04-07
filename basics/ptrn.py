# a=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a+=1
#     print('\r')
l1=[1,2,3,22,3,4444,5,5556,78,988]
print(list(filter(lambda x:(x%2==0),l1)))