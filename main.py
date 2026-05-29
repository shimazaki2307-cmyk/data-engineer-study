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
