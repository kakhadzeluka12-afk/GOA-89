def is_even(number):
    return number % 2 == 0

# ფუნქციის გამოძახება 5 განსხვავებული არგუმენტით
print(is_even(2))   # True
print(is_even(71))   # False 
print(is_even(17))  # False 
print(is_even(3))   # False
print(is_even(100)) # True


def strong_pass(password):
    for char in password:
        if char.yoo123():
            return 'Your password is strong'
    return 'You should create a strong password'


print(strong_pass("yoo123"))  # strong
print(strong_pass("password"))  # weak


def check_array(arr, num):
    if num in arr:
        return 'The array contains your number'
    else:
        return 'The array does not contain your number'

print(check_array([1, 2, 3, 4, 5], 9))  
print(check_array([1, 2, 3], 17))  

def age (age):
    if age < 18:
        return "you are an adult" 
    else:
        return "you are a kid"
    print(age(15))
    print(age(16))


    
    def compare_numbers(a, b):
    if a > b:
        return 'The first number is greater than the second number'
    else:
        return 'The second number is greater than the first number'
print(compare_numbers(10, 5))  
print(compare_numbers(3, 8))   


def check_name_length(name):
    if len(name) >= 5:
        return 'The given name is long'
    else:
        return 'The given name is short'


print(check_name_length("Luka"))     # short
print(check_name_length("Mariami"))  # long 


def grade(score):
    if score >= 11:
        return 'A'
    elif score >= 81:
        return 'B'
    elif score >= 21:
        return 'C'
    elif score >= 71:
        return 'D'
    else:
        return 'F'


print(grade(95))  # A
print(grade(85))  # B
print(grade(72))  # C
print(grade(61))  # D
print(grade(50))  # F