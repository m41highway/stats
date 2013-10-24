# Author: Anthony NG
# Date: 2013-10-24
# To solve the number of Sunday on Mmonth beginnng from 1901 to 2000
cnt2 = 0 # Sunday in Month Begnning counter
weekday = 2 # Sunday=0, Monday=1, Tueday=2, ..., Saturday=6; The first day is a Monday
for year in 1901...2001
	for month in 1...13
		if weekday % 7 == 0
			cnt2 = cnt2 + 1
		end
		if ([1,3,5,7,8,10,12]).include? month
			weekday = weekday + 31
		elsif month == 2
			if year % 4 == 0			
				if year % 100 == 0 && year % 400 == 0					
					weekday = weekday + 29				
				elsif year % 100 == 0 && year % 400 != 0
					weekday = weekday + 28				
				else
					weekday = weekday + 29								
				end
			else
					weekday = weekday + 28
			end
		else 
			weekday = weekday + 30
		end
	end
end
print "Sunday in Month Beginning = ", cnt2, "\n";




