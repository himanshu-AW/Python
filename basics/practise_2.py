# wap to detect double spaces ina given string
a=input("Enter a string with double spaces :")
ds=a.find("  ")
print(ds)
# IF in it have double spaces then replace it with single space
a=a.replace("  "," ")
print(a)