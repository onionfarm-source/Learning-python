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

print()

# Angles of a triangle

angle_1 = int(input("Please enter the first angle of the triangle "))
angle_2 = int(input("Please enter the second angle of the triangle "))
angle_3 = int(input("Please enter the third angle of the triangle "))

if angle_1 + angle_2 + angle_3 <= 180:
    print("These angles make a triangle")
else:
    print("Sorry, these angles do not make a triangle")

print()

# Max numbers

num_1 = int(input("Please enter the first number "))
num_2 = int(input("Please enter the second number "))
num_3 = int(input("Please enter the third number "))

if num_1 > num_2 and num_1 > num_3:
    print("The number {} is maximum".format(num_1))
if num_2 > num_1 and num_2 > num_3:
    print("The number {} is maximum".format(num_2))
if num_3 > num_1 and num_3 > num_2:
    print("The number {} is maximum".format(num_3))
if num_1 == num_2 == num_3:
    print("The numbers are equal")

print()

# Negative, Positive or Zero

number = int(input("Please enter a number "))
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
