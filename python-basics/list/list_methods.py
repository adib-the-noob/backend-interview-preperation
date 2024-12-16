# clear
fruites = ["apple", "banana", "cherry", "cherry", "cherry"]
fruites.clear()
print(fruites) # []


print("=====================================")
# count
fruites = ["apple", "banana", "cherry", "cherry", "cherry"]
print(fruites.count("cherry")) # 3 times

print("=====================================")
# adding elements of one to another list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

print("=====================================")

# index
list_adib = ["apple", "banana", "cherry"]
print(list_adib.index("banana")) # 1

print("=====================================")

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_number.index(5)) # 4

print("=====================================")

fruites_list = ["apple", "banana", "cherry", "cherry", "cherry"]
fruites_list.insert(0, "orange")

print(fruites_list) 

# pop
fruites_list.pop(0)
print(fruites_list)
fruites_list.remove("cherry")
print(fruites_list)

print("=====================================")

# reverse
hacker_list = ["apple", "banana", "cherry"]
hacker_list.reverse()
print(hacker_list)

print("=====================================")

# sort
cars  = ["Ford", "BMW", "Volvo"]
cars.sort()
print(cars)

print("=====================================")

def sortingFunc(e):
    return e['year']

cars = [
    {"car": "Ford", "year": 2005},
    {"car": "BMW", "year": 2011},
    {"car": "Volvo", "year": 2019}
]

cars.sort(key=sortingFunc)
print(cars)