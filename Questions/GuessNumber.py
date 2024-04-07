import random as r

# range = list(input("Range : "))
# min=range[0]
# max=range[1]

compGuss=r.randint(1,100)
user_target=0
while user_target!=compGuss:
    user_target=int(input("Enter Number: "))
    if(user_target<compGuss):
        print("U enterd lower Number, U should enter higher Number!")
    elif(user_target>compGuss):
        print("U enterd Higher Number, U should enter lower Number!")
    else:
        print("Hurry! , U gussed Coorect Number.")
