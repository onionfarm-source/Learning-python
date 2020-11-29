# Write a program to find maximum between three numbers.

# Write a program to check whether a number is negative, positive or zero.

# Write a program to check whether a number is even or odd.

# Write a program to check whether a year is leap year or not.

# Write a program to input angles of a triangle and check whether triangle is valid or not

# Write a program to find all roots of a quadratic equation.

# Write a program to calculate profit or loss. And determine which one it is.

########################################################################################################################

# Write the codes below
# Additional points for modulating each of the above code by a function call for ease of use in future case
# i.e not having to reinvent the wheel each and every time when needed.

# Even or Odd
number = int(input("Please enter a number "))
if number % 2 == 0:
    print("The number {} is even ".format(number))
else:
    print("The number {} is odd ".format(number))

# Angles of a triangle

angle_1 = int(input("Please enter the first angle of the triangle "))
angle_2 = int(input("Please enter the second angle of the triangle "))
angle_3 = int(input("Please enter the third angle of the triangle "))

if angle_1 + angle_2 + angle_3 <= 180:
    print("These angles make a triangle")
else:
    print("Sorry, these angles do not make a triangle")



