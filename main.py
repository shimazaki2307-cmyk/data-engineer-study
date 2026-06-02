print("データエンジニアになる")
name = "akira"
print(name)
age = 20
print(age + 5)
print("2026-05-25")
if age >=18:
    print("adult")
for i in range(5):
    print(i)

fruits =["apple","banana","orange"]
print(fruits)
print(fruits[0])
print(fruits[1])
for fruits in fruits:
    print(fruits)

def greet():
    print("hello")
greet()

def greet(name):
    print("hello " + name)
greet ("akira")

def add(a,b):
    return a + b
result = add(3,5)

print(result)

file = open("sample.txt","r")

text = file.read()
print(text)
file.close()

file = open("sample.txt","r")
for line in file:
    print(line)
file.close()

file = open("sample.csv","r")

for line in file:
    print(line)

file.close()

file = open("sample.csv","r")

for line in file:
    row = line.strip()
    print(row)

file.close()

file = open("sample.csv","r")

for line in file:
    row = line.strip().split(",")
    print("名前:",row[0],"年齢:",row[1])

file.close()

file = open("sample.csv","r")

for line in file:
    row = line.strip().split(",")
    
    if row[0] == "name":
        continue
    age = int(row[1])

    if age >= 30:
        print(row[0],age)

file.close()

file = open("sample.csv","r")

total_age = 0
count = 0

for line in file:
    row = line.strip().split(",")

    if row[0] == "name":
        continue

    age = int(row[1])

    total_age = total_age + age
    count += 1

print("合計年齢：",total_age)
print("平均年齢：",total_age / count)

file.close()


