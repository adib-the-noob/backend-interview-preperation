# variables
x, y, z = "Orange", "Apple" , "Banana"
print(x) # Orange
print(y) # Apple
print(z) # Banana

# Assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange


# Output variables
x = "Python"
y = " is "
z = "awesome"
print(x + y + z) # Python is awesome

# Global variables
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc() # Python is awesome

# Local variables
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc() # Python is fantastic