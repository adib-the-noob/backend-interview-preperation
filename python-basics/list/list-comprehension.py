fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newListWithA = []
for fruit in fruits:
    if "a" in fruit:
        newListWithA.append(fruit)
print(newListWithA)

# List comprehension
nameList = ["Hacker", "Earth", "Hello", "World"]
newListWithA = [name for name in nameList if "a" in name]
skipList = [name for name in nameList if name != "Earth"]
print(newListWithA)
print(skipList)

print("=====================================")
# List comprehension with if else
newList = [x for x in range(10)]
print(newList)

# accept number less then 7
newList = [x for x in range(10) if x <= 7]
print(newList)

print("=====================================")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # sort the list alphabetically
print(thislist)

print("=====================================")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True) # sort the list numerically
print(thislist)
print("=====================================")


# custom sort funtion
def myFunc(e):
    return abs(e - 50)

numlist = [100, 50, 65, 82, 23]
numlist.sort(key=myFunc)
print(numlist)

print("=====================================")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)