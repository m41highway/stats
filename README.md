In response to the question Counting Sundays from "http://projecteuler.net/problem=19". Here is the solution 
based on three different idea. First, "countSunday.rb" is coded in Ruby (as requested) which iterate the days
from the given period to set the weekday pointer, and thus the anwser is summerized through the itereation.
The second way is coded in the Python script "countSundayArray.py". I used NumPy multi-dimension array to 
store the days from the given period in sequence. Reshape the array to a 7 x n based array, and hence we can
get the rows where it is Sunday and January. We get the length of the result rows and know the answer. The third
way is coded in the Python script "countSundayWithObservation.py" which is based on the assumption (by observation) that
the number of sunday in January is ether 4 or 5, depends on what the first day is. A Sunday, Thursday or Friday 
1st of January has 5 Sunday, while a Monday, Tuesday, Wednesday or Saturday 1st of January has 4 Sunday. I made
a year array first to have the year and number of days. By observation that a leap year gives an offset of 2 weekdays
and a non leap year gives an offest of 1 weekday. I can then have the "year-first weekday" array. Hence, I can get 
the count of first day respectively for Monday, Tuesday to Sunday. And using the formula, 
total = sun * 5 + thr * 5 + fri * 5 + mon * 4 + tue * 4 + wed * 4 + sat * 4 to get the total.

"countSundayOnMonthBegin.rb" is the fixed version as there is mis-interpretation in question.

