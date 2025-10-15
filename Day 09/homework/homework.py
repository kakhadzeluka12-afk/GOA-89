my_list = ["apple", "banana", "strawberry","watermelon", "grape"]
index_to_delete =int(input("enter fruit (index) that u wanna delete:"))
if 0 <= index_to_delete < len(my_list):
       deleted_item = my_list.pop(index_to_delete)
       print("fruit was deleted: (deleted item)")
       print("wrong index")
       print("updated index (my_list)")


numbers = [1, 2, 3, 8, 90, 101, 1090, 909, 10001, 1009, 1008]

max_number =numbers[0]

for num in range(0): 
       if num > max_number:
        
        max_number = num

        print("the highest number is:", max_number)


my_list =[10, 20 , 30 , 40, 50]
slice_result = my_list[1:5]
print("slice [2-დან 5-მდე]:", slice_result)


masivi = [1, 2, 3]
new_value = 4
masivi = masivi + [new_value] 
print("დამატებული ელემენტი:", masivi)




masivi = [10, 20, 30, 40]
masivi.pop(2)  # წაშლის 30-ს

print("pop-ის შემდეგ:", masivi)
