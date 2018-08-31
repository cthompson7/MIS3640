# Exercise 2
#Rewrite calc.py to solve the following questions.

# 1.) How many seconds are there in 42 minutes 42 seconds?

totalSeconds = str((42*60) + 42)

print("There are " + totalSeconds + " seconds.")

# 2.) How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

totalMiles = str(10 / 1.61)

print("There are " + totalMiles + " miles in 10 kilometers.")

# 3.) If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

# Average Pace calculation

averagePaceInSeconds = ((42*60) + 42) / (10/1.61)

averagePaceInMinutes = averagePaceInSeconds / 60

avgPaceMinutesOnly = str(int(averagePaceInMinutes))

avgPaceSecondsOnly = str(round(60 - ((round(averagePaceInMinutes) - averagePaceInMinutes) * 60)))

print("Your average pace per mile is " + avgPaceMinutesOnly + " minutes and " + avgPaceSecondsOnly + " seconds.")

# Average Speed Calculation

milesPerHour = str((3600/((42*60) + 42)) * (10 / 1.61))

print("Your average speed in miles per hour is " + milesPerHour + ".")