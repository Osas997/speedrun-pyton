arr = ["apple", "banana", "cherry"]

p = [0,1,2,3]

p.sort(reverse=True)

print(p)

# foreach
for x in arr:
   print(x)

# for loop with index
for x in range(len(arr)):
   print("buah " + arr[x])

# while loop
i = 0
while i < len(arr):
   print(arr[i])
   i = i + 1

datas = [
   {
      "name": "budi",
      "age": 20
   },
   {
      "name": "bambang",
      "age": 21
   },
   {
      "name": "joko",
      "age": 22
   }
]

data = {
   "name": "popol",
   "age" : 23
}

datas.append(data)

# looping dictionary // json
for x in datas:
   print(x["name"])
