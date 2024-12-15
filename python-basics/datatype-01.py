x = "Hello, world"
y = 20
z = 20.5

x1 = 1j
x2 = ["apple", "banana", "cherry"] # list
x3 = ("apple", "banana", "cherry") # tuple
x4 = range(6) # range - a sequence of numbers starting from 0 by default and increments by 1 (by default), and ends at a specified number

print(x1)
print(x2)
print(x3)
print(x4)


y1 = {
    "name": "John",
    "age": 36
} # dict

y2 = {"apple", "banana", "cherry"} # set - every element is unique
y3 = frozenset({"apple", "banana", "cherry"}) # frozenset

print(y1)
print(y2)
print(y3)

z1 = b"Hello" # bytes
z2 = bytearray(5) # bytearray
z3 = memoryview(bytes(5)) # memoryview
print(z1)
print(z2)
print(z3)
