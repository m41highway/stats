# Author: Anthony Ng
# Date: 2013-10-23
# Sunday=0; Monday=1; Tuesday=2, ..., Saturday=6
import numpy as np
a = [] # an array to contain [year, total days, first weekday]
firstday = 2 # first day in 1901 is a Tuesday
for year in range(1901,2001):
    if year % 4 == 0:
        if (year % 100 == 0 and year % 400 == 0):
            a = np.append(a, [year,366, firstday % 7])
            firstday = firstday + 2
        elif (year % 100 ==0 and year % 400 != 0):    
            a = np.append(a, [year,365, firstday % 7])
            firstday = firstday + 1
        else:
            a = np.append(a, [year,366, firstday % 7])
            firstday = firstday + 2
    else:
        a = np.append(a, [year,365, firstday % 7])
        firstday = firstday + 1
array = np.array(a, dtype=np.int32)
year_array = array.reshape(len(array)/3, 3)
firstDayOnSun = year_array[year_array[0:,2] ==0] # Get the rows where first day is a Sunday
firstDayOnMon = year_array[year_array[0:,2] ==1] # Get the rows where first day is a Monday
firstDayOnTue = year_array[year_array[0:,2] ==2] # Get the rows where first day is a Tuesday
firstDayOnWed = year_array[year_array[0:,2] ==3] # Get the rows where first day is a Wednesday
firstDayOnThr = year_array[year_array[0:,2] ==4] # Get the rows where first day is a Thurday
firstDayOnFri = year_array[year_array[0:,2] ==5] # Get the rows where first day is a Friday
firstDayOnSat = year_array[year_array[0:,2] ==6] # Get the rows where first day is a Saturday

# By observation, January has 5 Sunday if the first day is a Sunday, Thurday, or Friday;
# And January has 4 Sunday if the first day is a Monday, Tuesday, Wednesday, or Saturday;
total = len(firstDayOnSun) * 5 + len(firstDayOnThr) * 5 + len(firstDayOnFri) * 5 + len(firstDayOnMon) * 4 + len(firstDayOnTue) * 4 + len(firstDayOnWed) * 4 + len(firstDayOnSat) * 4
print "Sunday in January = " + str(total)


