import random

string = "Hello World"  # String

# cek panjang string
print(len(string))

# mencari H dalam string dan mengembalikan index
print(string.find("H"))

# cek apakah ada "Hello" dalam string
if "Hello" in string:
   print("Yes")
else:
   print("No")

integer = 20  # int

flt = 20.5  # float

clx = 1j  # complex

arr = ["apple", "banana", "cherry"]  # list

print("panjang array = " , len(arr))

x = ("apple", "banana", "cherry")  # tuple

x = range(6)  # range

json = {
   "name": "John",
   "age": 36,
   "country": "Norway"
}  # dict

json["name"] = "Jane"

print(json["name"])

x = {"apple", "banana", "cherry"}  # set

randomNumber = random.randint(1, 10)

# print(randomNumber)