import datetime 

x=datetime.datetime.now()

print(x)
print(x.date())
print(x.time())
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%C"))
print(x.strftime("%D"))

x=datetime.datetime(2022,8,18)
print(x)
