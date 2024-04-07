# Inheritance means transfer of the characteristics of a class to other classes that are derived from it.
#  Inheritance are of three types
# <1> Single Inheritance
# <2> Multi-level inheritance
# <3> Multiple Inheritance

#  "Single Inheritance" -> means we can access a class in another class
class A:
    def displayA(self):
        print(" Hello A group in Single Inheritance")

class B(A):   # we can access "class A" characteristics in the "class B" i.e; B(A) and used accordingly
    def displayB(self):
        print(" Hello B group in Single Inheritance")

obj = B()  # creating only "class B" object
obj.displayA()  # calling "class A" directly without creating an object .
obj.displayB()  # calling "class B" simply


#  "Multi-level Inheritance" -> means we can access a class in another class & another class can also access in other class And So On..
# ( traverse in level wise i.e; from 1st-level to 2nd-level & from 2nd-level to 3rd-level & So on..  OR  we can say that Nested classes  )
class A:
    def displayA(self):
        print(" Welcome to class A in Multi-level Inheritance ")

class B(A):   # we can access "class A" characteristics in the "class B" i.e; B(A) and used accordingly
    def displayB(self):
        print(" Welcome to class B in Multi-level Inheritance")

class C(B):   # we can access "class A" as well as "class B" characteristics in the "class C" i.e; C(B) and used accordingly
    def displayC(self):
        print(" Welcome to class C in Multi-level Inheritance ")

obj = C()  # creating only "class C" object
obj.displayA()  # calling "class A" directly without creating an object .
obj.displayB()  # calling "class B" directly without creating an object .
obj.displayC()  # calling "class C" simply


#  "Multiple Inheritance" -> means we can Acces one or more classes in a particular class.
class A:
    def displayA(self):
        print(" Namestay from class A in Multiple Inheritance")

class B:   
    def displayB(self):
        print(" Namestay from class B in Multiple Inheritance ")

class C(A,B):   # we can access "class A" as well as "class B" characteristics in am"class C" i.e; C(B) and used accordingly
    def displayC(self):
        print(" Namestay from class C in Multiple Inheritance")

obj = C()  # creating only "class C" object
obj.displayA()  # calling "class A" directly without creating an object .
obj.displayB()  # calling "class B" directly without creating an object .
obj.displayC()  # calling "class C" simply