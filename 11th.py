"""mode = 'r', 'w', 'a', 'rb', 'wb', 'ab', 'r+', 'w+'

'r' = Read the files.
'w' = Write in files.
'a' = Append in files.
'rb' = read in binary.
'wb' = write in binary.
'ab' = append in binary.
'r+' = read and write both.
'w+' = write and read both.

1st Method to open the file.

f = open("file", "w")
f.write("Python is very eaisy language.\n")
f.write("C++ is dificult than Python.")
print("Writing Successfully")
f.close()

f = open("file")
data = f.read()
print(data)

2nd Method to open the file.

with open("file1", 'w') as f1:
    f1.write("Hello, I am second method to open the file.\n")
    f1.write("In second method no needs to close the file.")
    f1.close()

with open("file1") as f1:
    print(f1.read())

import csv

f = open("Student.csv", "w")
data = ["Rollno.", "Name", "Class"]
data1 = [1, "Aditi", "12th-A"]
data2 = [2, "Satyam", "12th-A"]
data3 = [3, "Arpana", "12th-A"]
data4 = [4, "Chesta", "12th-A"]
fwrite = csv.writer(f)
fwrite.writerow(data)
fwrite.writerow(data1)
fwrite.writerow(data2)
fwrite.writerow(data3)
fwrite.writerow(data4)
f.close()

f = open("Students.csv", "a")
data = [["Rollno.", "Name", "Class"],
    [1, "Aditi", "12th-A"],
    [2, "Arpana", "12th-A"],
    [3, "Chesta", "12th-A"]]
f.close()

f = open("Students.csv", "r")
fread = csv.reader(f)
for data in fread:
    print(data)
f.close()"""

# Examples of list:

# f = open("handle", "w")
# f.write("Hi I am Satyam\n")
# f.write("Hi Anuj\n")
# # print("Successfull print")
# f.close()

# f = open("handle", "a")
# f.write("hdghg")
# # print(f.read())
# f.close()

# f = open("handle")
# print(f.read())
# f.close()

# with open("sai", "w") as f1:
#     f1.write("fjfsfhs")

# with open("sai") as f1:
#     print(f1.read())

# Text file
# r,w,a,a+,w+,r+
# Binary File
# rb, wb, ab, ab+, wb+, rb+

# import pickle

# f = open("binary", "wb")
# lst = []
# name = 

# from tkinter import *
# root = Tk()
# root.geometry("700x500")
# root.title("GAME")
# def game():
#     print("When you play games")
# Label(root, text="Hi I am Your Assistant").pack()
# # Label(root)
# root.mainloop()
