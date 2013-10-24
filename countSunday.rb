cnt = 0 # Sunday in January counter
weekday = 1 # Sunday=0, Monday=1, Tueday=2, ..., Saturday=6; The first day is a Monday
for year in 1900...2001
	for month in 1...13
		if ([1,3,5,7,8,10,12]).include? month
			for day in 1...32	
				# Sunday in January ?
				if month == 1 and weekday % 7 == 0
					cnt = cnt + 1;   				
					print year , " " , month , " ", day, " " , weekday % 7 , " hit", "\n";
				else
					print year , " " , month , " ", day, " " , weekday % 7 , "\n";
				end 
				weekday = weekday + 1
			end
		elsif month == 2
			if year % 4 == 0			
				if year % 100 == 0 && year % 400 == 0
					for day in 1...30
						print year, " ", month, " ", day, " " , weekday % 7 , "\n";
						weekday = weekday + 1
					end				
				elsif year % 100 == 0 && year % 400 != 0
					for day in 1...29
						print year, " ", month, " ", day, " " , weekday % 7 , "\n";
						weekday = weekday + 1
					end				
				else
					for day in 1...30
						print year, " ", month, " ", day, " " , weekday % 7 , "\n";
						weekday = weekday + 1
			    		end								
				end
			else
				for day in 1...29
					print year, " ", month, " ", day, " " , weekday % 7 , "\n";
					weekday = weekday + 1
				end	
			end
		else 
			for day in 1...31
				print year, " ", month, " ", day, " " , weekday % 7 , "\n";
				weekday = weekday + 1
			end
		end
	end
end
print "Sunday in January counter = ", cnt, "\n";
print "total days = ", weekday, "\n";



