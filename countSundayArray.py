# Author: Anthony Ng
# Date: 2013-10-23
# To resolve the number of Sunday in January from 1901 to 2000
l = [] # Sunday in January counter
weekday = 1 # Sunday=0, Monday=1, Tueday=2, ... Saturday =6; The first day is a Monday
for year in range(1901,2001):
    for month in range(1,13):
        if month in (1,3,5,7,8,10,12):
            for day in range(1,32):
                l = np.append(l, [year, month, day, weekday%7])
                weekday = weekday + 1
        elif month == 2:
            if year % 4 ==0:
                if (year % 100 ==0 and year % 400 ==0):
                    for day in range(1,30):
                        l = np.append (l, [year, month, day, weekday%7])
                        weekday = weekday + 1
                elif (year % 100 ==0 and year % 400 != 0):
                    for day in range(1,29):
                        l = np.append(l, [year, month, day, weekday%7])
                        weekday = weekday + 1
                else:
                    for day in range(1,30):
                        l = np.append(l, [year, month, day, weekday%7])
                        weekday = weekday + 1
            else:
                for day in range(1,29):
                    l = np.append(l, [year, month, day, weekday%7])
                    weekday = weekday + 1
        else:
            for day in range(1, 31):
                l = np.append(l, [year, month, day, weekday%7])
                weekday = weekday + 1
array = np.array(l, dtype=np.int32)
calendar = array.reshape(len(array)/4 , 4)
sun = calendar[calendar[0:, 3] == 0 ]  # get the rows where Sunday
ans = calendar[sun[0:, 1] == 1] # get the rows where January
print "Sunday in January counter = " + str(len(ans))