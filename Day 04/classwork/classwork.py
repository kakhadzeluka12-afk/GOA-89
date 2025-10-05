num1 = float(input("9"))
num2 = float(input("7"))

f"{num1 + num2}\n"
f"{num2 +num1}\n"
f"{num1 -num2}\n"
f"{num1 * num2}\n"
f"{num1 / num2}\n"

x = "17"
x_int = int(x)
print(x_int)  # დაბეჭდავს: 17
# ტეკსტური სტრინგი "15" გადაიქცა მთელ რიცხვად

y = 17.9
y_int = int(y)
print(y_int)  # დაბეჭდავს: 17

a = "3.17"
a_float = float(a)
print(a_float)  # დაბეჭდავს: 3.17
# სტრინგი გარდაიქმნა float ტიპად

b = 17
b_float = float(b)
print(b_float)  # დაბეჭდავს: 17.0

num = 17
num_str = str(num)
print(num_str)  # დაბეჭდავს: "17"

num1 = input("15")

num2 = input("17")

num1 = float(num1)
num2 = float(num2)
 
print(num1 == num2)  # True თუ რიცხვები ტოლია
print( num1 != num2) # True თუ რიცხვები არ არის ტოლი
print( num1 > num2)  # True თუ num1 მეტია
print( num1 < num2)  # True თუ num1 ნაკლებია
print( num1 >= num2) # True თუ num1 მეტია ან ტოლია
print( num1 <= num2) # True თუ num1 ნაკლებია ან ტოლია

is_sunny = True      # ნიშნავს რომ ამინდი მზიანია
is_raining = False   # ნიშნავს რომ წვიმა არ მოდის


age = 20
is_adult = age >= 18 # ეს დააბრუნებს True რადგან 20 მეტია 18ზე

a = 5
b = 10

print(a < b)   # True, რადგან 5 ნაკლებია 10-ზე
print(a == b)  # False, რადგან 5 არ უდრის 10-ს
