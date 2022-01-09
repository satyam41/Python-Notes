"""Dictionary in Python:
A dictionary is an unordered and mutable Python container that stores mappings of unique keys to values. Dictionaries are written with curly brackets ({}), including key-value pairs separated by commas (,). A colon (:) separates each key from its value.

function in dictionary:
    1.dict.keys() - Returns a list conntaing the dictionary's keys.
    2.dict.vaues() - Returns a list conntaing the dictionary's values.
    3.dict.pop(key) - Remove the specific key items.
    4.dict.items() - Returns a list conntaing tuple for each key-value pair.
    5.dict.fromkeys(<argument>) - Returns a dictionary with the specified keys and value.
    6.dict.get(key) - Return the value of specific key.
    7.dict.update({key:value}) - Update the dictionary.
    8.dict.popitem() - Remove the items from the end of the dictionary.
    9.dict.setdefault(keyname, vlaue) - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
    10.dict.copy() - Copy the whole dictionary.
    11.dict.clear() - Clear the whole dictionary and returns empty dictionary.
"""

# Examples of Python Dictionary:

dic = {
    1:"Satyam",
    2:"Anubhav",
    3:"Anuj",
    4:"Sanmati",
    5:"Ojha"
}
print(dic)
print(dic.clear())
print(dic)