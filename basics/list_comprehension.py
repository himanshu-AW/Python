
l1=[x**2 for x in range(0,10) if x%2==0]
print(l1)

l2=[x*2 for x in range(1,11)]
print(l2)
# print numbers between 1 to 1000 which is divisible by 7
l3=[x for x in range (1,1001) if x%7==0]
print(l3)
# print number of vowels and consonents in a given string 
a=input("Enter a string : ")
v=['a','e','i','o','u']
l4=[x for x in a if x in v]
print("No of vowels in a given string : ",len(l4))
print("No of consonents in a given string : ",len(a)-len(l4))
# print numbers between 1 to 1000 which lies 4 in any number or any place ina digit
l5=[x for x in range (1,1001) if '4' in str(x)]
print(l5)
#print words which is equl to less then 5 in a given string 
a=input("Enter a string : ")
b=a.split()
l6=[x for x in b if 5<len(x)]
print(l6)
