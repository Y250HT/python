year = 2020
month = 2
if month in [1,3,5,7,9,12]:
    print("%d月有31天" % month)
elif month in [4,6,9,11]:
    print("%d月有30天" % month)
elif month == 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100!= 0:
        print("%d年%d月有29天" % (year,month))
    else :
        print("%d年%d月有28天" % (year,month))