# age = input('Please enter your age: ')

# if int(age) > 18:
#     print('adult')
# else:
#     print('teenager')

# if int(age) >= 18:
#     print('adult')
# elif int(age) >= 6:
#     print('teenager')
# else:
#     print('kid')

# weight = input('Please enter your weight: ')
# height = input("Please enter your height: ")

def calculate_bmi(weight, height):
    if (int(weight) / (int(height)**2))*703 >= 30:
        print("You are obese.")
    elif (int(weight) / (int(height)**2))*703 >= 25 and (int(weight) / (int(height)**2))*703 < 29.9:
        print("You are overweight.")
    elif (int(weight) / (int(height)**2))*703 >= 18.5 and (int(weight) / (int(height)**2))*703 < 24.9:
        print('You are normal weight.')
    else:
        print('You are underweight.')

# calculate_bmi(weight, height)

varA = 30
varB = 30

def variables_ab(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print('There are strings involved.')
    else:
        if varA > varB:
            print('Variable A is bigger.')
        elif varA < varB:
            print("Variable A is smaller.")
        else:
            print("Variable A is equal to Variable B.")

# variables_ab(varA,varB)

def diff21(n):
  if n>21:
    return 2*(abs(n-21))
  else:
    return abs(n-21)

def cigar_party(cigars, is_weekend):
  if is_weekend == True and cigars >= 40:
    return True
  elif is_weekend == True and cigars < 40:
    return False
  else:
    if is_weekend == False and cigars >= 40 and cigars <= 60:
      return True
    else:
      if is_weekend == False and cigars > 60 or cigars < 40:
        return False
