# Write a program to swap the values of three variables
# Initial values : a = 3 ,b = 2,c = 1
# Output : a = 1, b = 3, c = 2

# Write Code Below.

a = 3
b = 2
c = 1

a, b, c = c, a, b

print("a =", a)
print("b =", b)
print("c =", c)


# New Test Values :
# input : a = 218, b = 417, c = 301
# Output : a = 417; b = 301; c = 218;

# Write Code Below.

a = 218
b = 417
c = 301

print("a = {}".format(b))
print("b = {}".format(c))
print("c = {}".format(a))
### a, b, c values not swapped.

a = 218
b = 417
c = 301

a, b, c = b, c, a
print("a =", a)
print("b =", b)
print("c =", c)

# Write a program to swap the values of three variable(values of a, b, c should be user-given at run time)
# Additional Points, for using Method/function Call in the program.
# Write Code Below.
