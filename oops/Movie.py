class Movie :
    def __init__(self,title,hero,heroine):
        self.hero=hero
        self.title=title
        self.heroine=heroine
    def info(self):
        print("Title : ",self.title)
        print("the name of hero: ",self.hero)
        print("the name of heroine  : ",self.heroine)

lom=[]
while(True):
    title=input("Enter titile : ")
    hero=input("Enter Name of Hero : ")
    heroine=input("Enter Name of Heroine: ")
    m=Movie(title,hero,heroine)
    lom.append(m)
    option=input('Do you want to enter more info:[Y/N]')
    if option.lower()=='n':
        break
print('#'*30)
print('Movies infomation')
for i in lom:
    i.info()