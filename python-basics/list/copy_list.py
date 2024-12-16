myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newList = myList.copy()
print(newList)

# or
newList2 = list(myList)
print(newList2)

# or
newList3 = myList[:] # slicing
print(newList3)


print("=====================================")

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

print(list1 + list2) # ['a', 'b', 'c', 1, 2, 3]

print("=====================================")

testList = ["Hacker", "Earth", "Hello", "World"]
testList2 = ["Data", "Science", "Machine", "Learning"]

for i in testList2:
    testList.append(i)

print(testList)