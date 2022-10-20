import random

# shopping_list = [
#     "oranges",
#     "Cat food",
#     "Sponge cake",
#     "long-grain rice",
#     "cheese board"
#     ]
#
# print(shopping_list[1])
#
# chocolates = {
#     "white": 1.50,
#     "milk": 1.20,
#     "dark":1.80,
#     "vegan":2.00
# }
#
# choc_choice = input("Which chocolate would you like? ")
# print(chocolates[choc_choice])

ticket = [3, 14, 24, 37, 44, 68, 70]

winners = [random.randint(0, 70) for _ in range(7)]
print(winners)







