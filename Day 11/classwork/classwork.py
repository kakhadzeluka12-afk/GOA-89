# 1 დავალება

def greet(name):
    print("Hello " , + name)
        
    greet("Luka")

# 2 დავალება

def add(num1 , num2):
   
   # ორი არგუმენტების ჯამი
   print("total is: ",  + num1 + num2 )
    
    # ფუნქციის გამოძახება არგუმენტებით
add (10 , 17)
add (8 , 17)

# 3 დავალება 
def add (num1 , num2): 
         return num1 + num2 
def multiply (num1 , num2): 
         return num1 * num2 
sum_result = add(1,17)

product_result = multiply(5,17)
sum_result + product_result 
print(sum_result)
print(product_result)

# 4 დავალება 

def filter_evens(limit):
      even_numbers = []
      for i in range(0, limit + 1):
       if i % 2 == 0:

        even_numbers.append(i)

       return even_numbers 
       result + filter_evens(20)
       print("even numbers up to 20: " ,  + result)
      
      