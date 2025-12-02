# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
extreme = ""

temp = int(input("What temperature is it today? (Fahrenheit):  "))
adj = " "
if temp >= 110 or temp <= -10:
    extreme = True
if temp >= 80:
    adj = "hot"
if temp >= 60 and temp < 80:
    adj = "warm"
if temp >= 50 and temp < 60:
    adj = "cool"
if temp >= 35 and temp < 50:
    adj = "chilly"
if temp < 35:
    adj = "cold"
print(f"It is {temp} degrees outside. That's {adj}.")
if extreme == True:
    print("The temperature is extreme!")

# list = [1,2,3,4,5]
# list2 = [list]*5
# list3 = [list2]*5
# print(list3)
# list4 = [list3]*7
# print(list4)