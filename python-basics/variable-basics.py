x = "awesome"

def myFunc():
    global x
    x = "fantastic"
    print("Python is " + x)

print(x) 
myFunc()