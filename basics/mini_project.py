grade=input("Enter the grade of faculty : ")
exp=int(input('Enter the the experiance : '))
month=input('Enter the month : ')
l31=['januray','march','may','july','august','october','december']
nod=int(input('Enter the number of days present : '))
if grade=='p':
    bsal=40300
    da=bsal*.35
    hra=bsal*.15
    agp=10000
    sal=bsal+da+hra+agp
    gsal=sal*float((1+10/100))**(exp*100)
    anlsal=gsal*12
    if anlsal<=500000:
        tax=anlsal*.1
    elif anlsal>500000 or anlsal<=700000:
        tax=anlsal*.15
    elif anlsal>700000 or anlsal <=900000:
        tax=anlsal*.2
    else:
        tax=anlsal*.3
    tpm=tax//12
    netsal=gsal-tpm
    if month in l31:
        extsal=nod*(netsal/31)
    else:
        extsal=nod*(netsal/30)
elif grade=='asp':
    bsal=35000
    da=bsal*.35
    hra=bsal*.15
    agp=8000
    sal=bsal+da+hra+agp
    gsal=sal*float((1+10/100))**(exp*100)
    anlsal=gsal*12
    if anlsal<=500000:
        tax=anlsal*.1
    elif anlsal>500000 or anlsal<=700000:
        tax=anlsal*.15
    elif anlsal>700000 or anlsal <=900000:
        tax=anlsal*.2
    else:
        tax=anlsal*.3
    tpm=tax//12
    netsal=gsal-tpm
    if month in l31:
        extsal=nod*(netsal/31)
    else:
        extsal=nod*(netsal/30)
elif grade=='r':
    bsal=28000
    da=bsal*.35
    hra=bsal*.15
    agp=6000
    sal=bsal+da+hra+agp
    gsal=sal*float((1+10/100))**(exp*100)
    anlsal=gsal*12
    if anlsal<=500000:
        tax=anlsal*.1
    elif anlsal>500000 or anlsal<=700000:
        tax=anlsal*.15
    elif anlsal>700000 or anlsal <=900000:
        tax=anlsal*.2
    else:
        tax=anlsal*.3
    tpm=tax//12
    netsal=gsal-tpm
    if month in l31:
        extsal=nod*(netsal/31)
    else:
        extsal=nod*(netsal/30)
elif grade=='asp':
    bsal=25000
    da=bsal*.35
    hra=bsal*.15
    agp=5000
    sal=bsal+da+hra+agp
    gsal=sal*float((1+10/100))**(exp*100)
    anlsal=gsal*12
    if anlsal<=500000:
        tax=anlsal*.1
    elif anlsal>500000 or anlsal<=700000:
        tax=anlsal*.15
    elif anlsal>700000 or anlsal <=900000:
        tax=anlsal*.2
    else:
        tax=anlsal*.3
    tpm=tax//12
    netsal=gsal-tpm
    if month in l31:
        extsal=nod*(netsal/31)
    else:
        extsal=nod*(netsal/30)
print("the exect salary is : ",extsal)