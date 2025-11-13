# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
print(10 > 5)
print(7 == 2 * 3 + 1)
print(8 != 8)
print(4 <= 2 + 2)

# Write 3 examples that result in True and 3 that result in False.

print(989449432049392<5)
print(893<1)
print(5>48)
print(234567890>3)
print(3>-99)
print(9839324938989049032498439-9839324938989049032498439==0)

# Create a simple grade-checking condition:

grade = int(input("What's your current grade? (integer):   "))
if grade < 0:
    print("You can't have that...")
else:
    if grade > 60:
        if 70 > grade >= 60:
            print("You have a D.")
        else:
             if 80 > grade >= 70:
                 print("You have a C.")
             else:
                  if 90 > grade >= 80:
                      print("You have a B.")
                  else:   
                      if 100 >= grade >= 90:
                        print("You have an A!")
                      else: 
                          if 100 < grade:
                             print("Nice! You have better than an A!")
    else:
        print("You're failing...")
            # if 80 > grade >= 70:
            #      if 90 > grade >= 80:
            #           if 100 >= grade >= 90:
            #                if grade > 100:
            #                     print("Nice! You have better than an A!")
                      
# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.

password = input("LELELELEL   ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Ok yay")
else:
    print("i hate you and want you to die")