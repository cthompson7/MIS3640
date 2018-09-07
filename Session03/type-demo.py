
# age = int(input('Please enter your age '))
#
# if age >= 21:
#     print('Yes, you can.')
# else:
#     print('sorry, you cannot.')


# 3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”,
    #which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
    #Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus
    #the number of days since the epoch.

import time
tt = time.time()
1437746094.5735958

days = (tt / (60*60*24))
numOfDays = int(days)

hours = (days % numOfDays)*24
numOfHours = int(hours)

minutes = (hours % numOfHours)*60
numOfMinutes = int(minutes)

seconds = (minutes % numOfMinutes)*60
numOfSeconds = int(seconds)

print("The current time is: {} hours, {} minutes, and {} seconds. The number of days since the epoch is: {}.".format(numOfHours,numOfMinutes,numOfSeconds,numOfDays))
