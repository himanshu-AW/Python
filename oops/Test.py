# class Test:
#     x=10
#     def __init__(self):
#         self.y=20
# t1=Test()
# t2=Test()
# print('for t1 ',t1.x,t1.y)
# print('for t2 ',t2.x,t2.y)
# t1.x=888
# t2.y=999
# print('for t1 ',t1.x,t1.y)
# print('for t2 ',t2.x,t2.y)

# class test1:
#     def __init__(self):
#         self.a=12
#         self.b=23
#     def m1(self):
#         self.c=55

# t1=test1()
# t1.m1()
# t2=test1()
# t2.d=66
# print(t1.__dict__)
# print(t2.__dict__)

# class testDemo:
#     def __init__(self):
#         self.a=33
#         self.b=45
#     def m(self):
#         print(self.a)
#         print(self.b)
# t=testDemo()
# t.m()
# print(t.a)
# print(t.b)

# # how to delete instance VAR 
# class Tests:
#     def __init__(self):
#         self.a=12
#         self.b=23
#         self.c=10
#         self.d=20
#     def m1(self):
#         del self.a

# t=Tests()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.b
# print(t.__dict__)

# class T:
#     def __init__(self):
#         self.c=30
#         self.d=40
#         self.a=10
#         self.b=20
#     def m1(self):
#         del self.a

# t1=T()
# t2=T()
# del t1.a
# print(t1.__dict__)
# print(t2.__dict__)


# class T2:
#     def __init__(self):
#         self.a=10
#     def m1(self):
#         self.a=20
#         self.b=30

# t=T2()
# t.m1()
# t.a=40
# t.c=50
# print(t.__dict__)

# class Tst:
#     a=10
#     def __init__(self):
#         Tst.b=20
# t=Tst()
# # print(t.__dict__)
# print(Tst.__dict__)

class demo:
    a=20
    def m1(self):
        self.a=888
t=demo()
t.m1()
print(demo.a)
print(t.a)