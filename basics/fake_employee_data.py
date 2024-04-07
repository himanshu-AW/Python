from random import *
s="zxcvbnmsdfghjklqwertyuiop"
city=['Delhi','Mumbhai','Ghaziabad','Gujrat','Rajistan','Ahmedabad','Ajmer','Hyderabad','Agra','Bangalore']
designation=['Manager','Accountant','Assistant Manager','Clark','Salesman','Analyst','Peon','Ass Exec Eng','Chief Engineer','Receptionist'] 

def get_fack_name():
        name=choice(s).upper()
        n=randint(2,9)
        for i in range(n):
            name=name+choice(s)
        return name
    
def get_emp_number():
        print('The Employe ID Number : en - ',end='')
        for i in range (4):
            n=randint(0,4)
            print(n,end='')
        print()
    
def get_emp_salary():
        print(f'The Employee Salary : {round(uniform(10000,50000),3)}')

data=500
while data>0:
    print('The Fake Employee Name : ',get_fack_name())
    get_emp_number()
    get_emp_salary()
    print('The Employee Designation : ',choice(designation))
    print('The Employee City : ',choice(city))
    print()
    data-=1