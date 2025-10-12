# ახსენით  რა განსხვავებაა while loop  და for loop ის შორის

# for loop მაგალითად მიუთითებ 15ს და დაწერს 15 სიტყვას რასაც ჩაწერ დაბეჭვდაში მაგალითად ასე,
for i in range(15):
    print("Luka")
#  ეს დაბეჭდავს "luka" 15ჯერ.

# while loop  ის აგრძელებს მუშაობას სანამ მაგალითშ არ გამოისახება True.

x = 1
while x < 100:
    x * 2

i = 0
while i < 0:
    print(i)
    i = i + 1



for i in range ( 1, 11):
     if i == 7:
       break
     print(i)


for i in range ( 1 , 51):
     if i % 4 == 0:
         print(i)



name = input("Enter your name: ")
lastname = input("Enter your lastname: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

print("You are {name}")
print("Your lastname is {lastname}")
print("You are {age} years old")
print("You live in {country}")



i = 0
sum = 0

while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("Sum of even numbers:", sum)