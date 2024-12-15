
#    0 1 2(l) 3(l) 4(o) 5    
b = "Hello, world!"
print(b[2:5]) # llo

# 2:5 -> 2 is starting index and 5 is ending index

print(b[:5]) # Hello -> 0:5 -> 0 is starting index and 5 is ending index
print(b[2:]) # llo, world! -> 2: -> 2 is starting index and no ending index
print(b[-5:-2])

txt = "hello, World"
print(txt.upper())
print("HELLO, WORLD".lower())

sample_txt = "  Hello, World!  "    
print(sample_txt.strip()) # "Hello, World!"


# Replace string
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!

smple = "Hello, World!"
xy = smple.split(",")
yz = smple.split(",")[0]

print(xy)
print(yz)

# concatenation
a = "hello"
b = "Word"
c = a + " " + b

print(c)

print("2" + "2")
