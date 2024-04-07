def checkYear(year):
    if year%400==0 or year%100!=0 and year%4==0:
        print(f"{year} leap year ")
    else:
        print(f"{year} Not leap year")

checkYear(2000)
checkYear(1900)
checkYear(2010)
checkYear(2020)
checkYear(2024)
checkYear(1919)