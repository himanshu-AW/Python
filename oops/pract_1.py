class Student:
    def __init__(self):
        print('constructor executes')
        self.name =name
        self.rollno =rollno
        self.marks = marks

    def talk(self):
        print('My Name is ',self.name)
        print('My Roll no. is ',self.rollno)
        print('My Marks are ',self.marks)
s=Student()
# print(s.name)
# print(s.rollno)
# print(s.marks)
s.talk()

s1=Student()
s2=Student()
s3=Student()
s1.talk()
s2.talk()
s3.talk()