# ჩემი აზრით list არის სია რომელშიც შეგვიძლია შევინახოთ ბევრი სხვადასხვა მონაცემთა ტიპები.
# კი list შეგვიძლია შევინახოთ ბევრი სხვადასხვა მონაცემთა ტიპები.

my_list = []
for i in range (5):
    my_list = int(input("enter the number: "))
    my_list.append (21)
    print(my_list)

#  თქვენი სიტყვებით რა არის index-indexing  
# ინდექსირებდა გეხმარება დიდი რაოდენობის მონაცემებიდან სწრაფად ვიპოვოთ ის რაც გვჭირდება


family = ["dad","mom","sister"]
print(family[0])
print(family[1])
print(family[2])

# 6) არის თუ არა ქვემოთ მოცემულ კოდში შეცდომა

name = 'Nino'
name[1] = 'a'
# მოცემუმ კოდში შეცდომა ის არის რომ ნინო-ში არ არის ასო ა რომ დაწერო ა გამოიტანს ნანოს და არა ნინოს

my_list = [1,2,3,4,5]
my_list[4] = 5

mixed_list = [17, "hello", False, 1.17, None]

for item in mixed_list:
    print(item)