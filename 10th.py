"""Scicing in Python:

Specify the start index and the end index, separated by a colon, to return a part of the string.

Syntax:
listName/stringName/dictionaryName/tupleName[start:stop:step]

Slice From the Start
By leaving out the start index, the range will start at the first character:

a = "Hello, World!"
print(a[:5]) 

# Output:
Hello

Slice To the End
By leaving out the end index, the range will go to the end:

a = "Hello, World!"
print(a[2:]) 

# Output:
llo, World!

Negative Indexing
Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

# Output
orl
"""