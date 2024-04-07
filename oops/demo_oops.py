class DemoClass:   # DemoClass is a class  in " CamelCase " 
    a=10   #  variable in class

    # NOTE_POINT :   one argument is neccessary passing in methods or constructor i.e; we consider ' self ' as argument   
    
    def __init__(self):   # __init__(self) is a Constructor 
        print('****** Welcome to our World *******')

    def  sumvalue(self):  # Methods ( Function) in class without argument
        a,b=12,23
        print(a+b)

    def  sumvalue1(self,a,b):  # Methods ( Function) in class with argument  i,e;  a,b are two arguments
        print(a+b)
        
    def showvalue(self): 
        print(self.a)

    def showvalue1(self):
        self.c=self.a*self.a
        print(self.c)

obj=DemoClass()  # obj is a object
print(obj.a)     # We can acccess variables from tha class by using object_name.variable_name

obj.sumvalue()     # methods (Function) calling such as object_name.method_name() without argument

obj.sumvalue1(40,34)     # methods (Function) calling such as object_name.method_name() with arguments

obj.showvalue()  # methods (Function) calling to  Access veriables which is decleared in class

obj.showvalue1()  # methods (Function) calling ,  operation performed of veriable which is decleared in class
