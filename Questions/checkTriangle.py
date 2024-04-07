def checkTriangle(a,b,c):
    if(a==b==c):
        print ("equilateral triangle.")
    elif ((a==b and a!=c) or (a!=b and b==c) or (a==c and a!=b)):
        print("Isosceles triangle.")
    elif(a!=b!=c):
        print("Scalene triangle.")

checkTriangle(1,2,3)
checkTriangle(2,2,3)
checkTriangle(3,3,3)


x,y=10,20
print("sum of "+str(x)+" and "+str(y)+" is ", x+y)