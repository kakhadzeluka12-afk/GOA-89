#კვადრატების ჯამი 
sum_of_squares= 0
for i in range(1 , 11):
    sum_of_squares =+ i ** 2
    print (sum_of_squares)

#შეამოწმეთ იყოფა თუ არა 3ზე

total_count = 0
for i in range (1,100):
    1 , 100  % 3
    print(total_count)

#sum_of_odds

sum_of_odds = 0
for i in range (1,101):
  if i % 2  == 1:
     sum_of_odds += i
     print(sum_of_odds)


# შემოატანინეთ მომხმარებელს რიცხვი
number = int(input("შეიყვანეთ რიცხვი: "))
for i in range(1 ,number + 1):
      print(i)


# დაბეჭდებ რიცხვი იმდენჯერ რამდენი ციფრიც შემოიტანა მომხმარებელმა

number = int(input("შეიყვანეთ რიცხვი: "))

for i in range(number):
    print("Hello")

# ახსენით რა არის while loop  და for loop კომენტარის სახით:

# while loop არის რომელიც მუშობს სანამ ეკრანზე მოცემული პირობა სიმართლეა ანუ true 

# for loop არის ციკლი რომელიც გამოიყენება ტეკსტის  რამდენიმეჯერ დასაბეჭდათ 



# while loop გამოყენებით დაბეჭდეთ რიცხვი 1-10

i = 1
while i <= 10:
    print(i)
    i += 1

# 10
num =int(input("შეიყვანეთ ნებისმიერი რიცხვი: "))

if num < 0:
    print("რიცხვი უარყოფითია")
elif num > 0:
    print("რიცხვი დადებითია")
else:
    print("რიცხვი ნულია")