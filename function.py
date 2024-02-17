x = "keren"

def fungsi():
   global x # variable global
   x = "asu" # variable local
   print("pyton " + x)

def sum(x, y):
   print("sum = " , x + y)

input1 = int(input("angka 1 = "))
input2 = int(input("angka 2 = "))

sum(input1, input2)

# print(sum(x = 10,y = 10))
# print("pyton " + x)

