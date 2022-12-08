import array
month=array.array('i',[0,31,28,31,30,31,30,31,31,30,31,30,31])
count=0
d=int(input("Enter a day:"))
months=int(input("Enter a month:"))
year=int(input("Enter a year:"))
days=int(input("Enter number of days to find out the future date:"))
if year%4==0:
    month[2]=28
while count<days:
    d=d+1
    count=count+1
    if d>month[months]:
        d=1
        months=months+1
    if months>12:
        months=1
        year=year+1
        if year%4==0:
            month[2]=29
        else:
            month[2]=28
print("Future date= ", end='')
print(d,end='-')
print(months,end='-')
print(year)