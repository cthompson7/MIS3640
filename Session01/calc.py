# Exercise 2
#Rewrite calc.py to solve the following questions.

# # 1.) How many seconds are there in 42 minutes 42 seconds?
#
# totalSeconds = str((42*60) + 42)
#
# print("There are " + totalSeconds + " seconds.")
#
# # 2.) How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
#
# totalMiles = str(10 / 1.61)
#
# print("There are " + totalMiles + " miles in 10 kilometers.")
#
# # 3.) If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
#
# # Average Pace calculation
#
# averagePaceInSeconds = ((42*60) + 42) / (10/1.61)
#
# averagePaceInMinutes = averagePaceInSeconds / 60
#
# avgPaceMinutesOnly = str(int(averagePaceInMinutes))
#
# avgPaceSecondsOnly = str(round(60 - ((round(averagePaceInMinutes) - averagePaceInMinutes) * 60)))
#
# print("Your average pace per mile is " + avgPaceMinutesOnly + " minutes and " + avgPaceSecondsOnly + " seconds.")
#
# # Average Speed Calculation
#
# milesPerHour = str((3600/((42*60) + 42)) * (10 / 1.61))
#
# print("Your average speed in miles per hour is " + milesPerHour + ".")


# Exercise 1 for Session 02

# 1.) The volume of a sphere with radius r is
    #(4/3)πr3.

    #What is the volume of a sphere with radius 5?

import math
radius = 5
volume = (4/3)*(math.pi)*(radius**3)

print('The volume of a sphere with radius 5 is', volume)

# 2.) Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount.
    #Shipping costs $3 for the first copy and 75 cents for each additional copy.
    #What is the total wholesale cost for 60 copies?

numberOfBooks = 60
wholesaleCost = (24.95-(24.95*.4))*numberOfBooks + (numberOfBooks-1 *.75)

def wholesaleTotal(wholesaleCost):
    if numberOfBooks >= 1:
        return wholesaleCost + 3.00
    else:
        return wholesaleCost

print("The total wholesale cost for 60 copies is: ${:.2f}".format(wholesaleTotal(wholesaleCost)))

# 3.) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
    #then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
    #what time do I get home for breakfast?

easy_pace = 8*60 + 15
tempo_pace = 7*60 + 12
total_time = 2*easy_pace + 3*tempo_pace
timeInMinutes = round(total_time/60)
timeInSecs = ((total_time/60 - round(total_time/60)) *60)
startHour = 6
startMinute = 52

def minutes(timeInMinutes, startMinute):
    endMinute = 0
    if startMinute + timeInMinutes > 60:
        endMinute = startMinute + timeInMinutes - 60
        return endMinute
    else:
        endMinute = startMinute + timeInMinutes
        return endMinute

def hours(startHour):
    additionalhours = 0
    endHour = 0
    if startMinute + timeInMinutes > 60:
        additionalhours = additionalhours + 1
    endHour = additionalhours + startHour
    return endHour

print("You get home for breakfast at {}:{}am.".format(hours(startHour),minutes(timeInMinutes, startMinute)))

# 4.) If my average grade rises from 82 to 89. What is the percentage of the increase?
    #Format the result as 'xx.x%'. Keep one figure after decimal point.

changeInGrade = (89-82)
percentIncrease = (changeInGrade / 82) * 100

print("The percentage of the increase is {:.1f}%.".format(percentIncrease))


